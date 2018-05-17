# -*- coding: utf-8 -*-
import codecs
import json
from  xpc import items,pipelines,middlewares
import scrapy
# 使用RedisSpider替换scrapy.Spider  同时删除start_urls.
# 在redis中插入  name:start_urls 值作为start_urls.
from scrapy_redis.spiders import RedisSpider
from scrapy import Request


class DiscoverySpider(RedisSpider):
    name = 'discovery'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/sort-like?from=tabArticle']
    composer_url = 'http://www.xinpianchang.com/u%s?from=articleList'

    def parse(self, response):
        pid_list = response.xpath("//ul[@class='video-list']/li/@data-articleid").extract()
        # //ul[@class='video-list']/li/@data-articleid
        thumbnail_list = response.xpath("//a[@class='video-cover']/img/@_src").extract()
        # print(thumbnail)
        # print(len(pid_list))
        url = 'http://www.xinpianchang.com/a%s'
        comment_url = 'http://www.xinpianchang.com/article/filmplay/ts-getCommentApi/id-%s/page-%s'
        # http://www.xinpianchang.com/article/filmplay/ts-getCommentApi/id-10214584/page-2/pagesizi-10
        for num, pid in enumerate(pid_list):
            req = Request(url % pid, callback=self.parse_post)
            req.meta['pid'] = pid
            req.meta['thumbnail'] = thumbnail_list[num]
            yield req
            req_comment = Request(comment_url % (pid,'1'), callback=self.parse_comment)
            req_comment.meta['id'] = pid
            yield req_comment
        next_page = response.xpath('//div[@class="page"]/a[last()]/@href').get()
        if next_page:
            yield response.follow(next_page,callback=self.parse)
        # for pid in pid_list:
        #     req_comment = Request(comment_url % pid, callback=self.parse_comment)
        #     req_comment.meta['id'] = pid
        #     yield req_comment

    def parse_post(self, response):
        # print(response.url)
        post = items.PostItem()
        post['thumbnail'] = response.meta['thumbnail']
        post['pid'] = response.meta['pid']
        post['title'] = response.xpath("//div[@class='title-wrap']/h3/text()").get()
        post['preview'] = response.xpath('//div[@class="filmplay"]//img/@src').extract_first()
        post['video'] = response.xpath("//source/@src").get()
        cates = response.xpath("//span[@class='cate v-center']/a/text()").extract()
        for i in range(len(cates)):
            cates[i] = cates[i].strip()
        post['category'] = '-'.join(cates)
        # 缩略图
        # post['thumbnail'] = response.xpath("//img[@class='lazy-img lazy-img-show']/@src").extract()
        # 发布时间
        post['created_at'] = response.xpath("//span[@class='update-time v-center']/i/text()").get()
        # 播放次数
        post['play_counts'] = response.xpath("//div[@class='filmplay-data-play filmplay-data-info']//i/text()").get().replace(',','')
        # 点赞次数
        post['like_counts'] = response.xpath("//span[@class='like-btn  v-center']/span/@data-counts").get()
        # 描述
        post['description'] = response.xpath("//div[@class='filmplay-info-desc left-section']/p/text()").get()
        if post['description'] is not None:  # 去除\t \n等无用字符
            post['description'] = post['description'].strip()

        yield (post)

        creator_list = response.xpath("//div[@class='user-team']/div/ul/li")
        for a in creator_list:
            cr = items.CopyrightItem()
            cr['cid'] = a.xpath("./a/@data-userid").get()
            cr['pid'] = post['pid']
            cr['pcid'] = cr['cid']+'_'+cr['pid']
            cr['roles'] = a.xpath("./div/span/text()").get()
            yield cr
            post_req_composer = Request(self.composer_url % cr['cid'], callback=self.parse_composer)
            post_req_composer.meta['cid'] = cr['cid']
            yield post_req_composer
            # yield response.follow(self.composer_url % cr['cid'], callback=self.parse_composer)
        # cr = {}
        # cr['cid'] = response.xpath("//div[contains(@class,'filmplay-creator')]//li/a/@data-userid").get()
        # cr['pid'] = post['pid']
        # cr['roles'] = response.xpath("//div[contains(@class,'filmplay-creator')]//li/div/span/text()").get()
        # yield response.follow(composer_url % cr['cid'],callback=self.parse_composer)

    def parse_composer(self, response):
        composer_list = items.ComposerItem()
        composer_list['cid'] = response.meta['cid']
        composer_list['banner'] = response.xpath("//div[@class='banner-wrap']/@style").get()[21:-1]  # banner[21:-1]
        composer_list['avatar'] = response.xpath("//span[@class='avator-wrap-s']/img/@src").get()
        composer_list['name'] = response.xpath("//div[@class='creator-info']/p[1]/text()").get()
        composer_list['intro'] = response.xpath("//div[@class='creator-info']/p[2]/text()").get()
        composer_list['like_counts'] = response.xpath("//span[contains(@class,'like-counts')]/text()").get().replace(
            ',', '')
        composer_list['fans_counts'] = response.xpath("//span[contains(@class,'fans-counts')]/text()").get().replace(',','')
        composer_list['follow_counts'] = response.xpath("//span[@class='follow-wrap']/span[2]/text()").get()
        composer_list['location'] = response.xpath(
            "//span[contains(@class,'icon-location')]/following-sibling::span[1]/text()").get()
        composer_list['career'] = response.xpath(
            "//span[contains(@class,'icon-career')]/following-sibling::span[1]/text()").get()
        yield composer_list

    # http://www.xinpianchang.com/u10000475?from=articleList
    # 导航背景图 banner
    # 作者名  name
    # 作者头像  avatar
    # 作者简介  intro  可能为空
    # 人气 like_counts
    # 粉丝 fans_counts
    # 关注 follows_counts
    # 所在地 location  可能为空  相邻的第一个span标签following-sibling::span[1]
    # 职业 career  可能为空 [contains(@class,'classname')]
    # parse_composer

    def parse_comment(self, response):
        # print(response.url)
        # obj = json.dumps(response.text,ensure_ascii=False)
        # fp = codecs.open('output.txt', 'a+', 'utf-8')
        # fp.write(obj)
        # fp.close()
        obj = json.loads(response.text)
        next_page_url = obj['data']['next_page_url']
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse_comment)
        total = obj['data']['total']
        total_page = obj['data']['total_page']
        comment_list = obj['data']['list']
        # print(len(comment_list))
        # id = response.meta['id']
        # print('id是:%s,评论%s条'% (count,len(comment_list)))
        # print(obj['data']['next_page_url'])
        # username_list = {}

        for ccc in comment_list:
            comment = items.CommentItem()
            comment['commentid'] = ccc['commentid']
            comment['pid'] = ccc['articleid']
            comment['content'] = ccc['content']
            comment['like_counts'] = ccc['count_approve']
            comment['created_at'] = ccc['addtime']
            comment['cid'] = ccc['userInfo']['userid']
            comment['uname'] = ccc['userInfo']['username']
            comment['avatar'] = ccc['userInfo']['face']
            if ccc['reply']:
                comment['reply'] = ccc['reply']['commentid']
            yield comment
            comment_req_composer = Request(self.composer_url % comment['pid'], callback=self.parse_composer)
            comment_req_composer.meta['cid'] = comment['cid']
            yield comment_req_composer
        # json.dump(obj, f)
