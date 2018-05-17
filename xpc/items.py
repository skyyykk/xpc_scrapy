# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 视频信息
class PostItem(scrapy.Item):
    # define the fields for your item here like:
    table_name = 'posts'

    pid = scrapy.Field()
    title = scrapy.Field()
    thumbnail = scrapy.Field()
    preview = scrapy.Field()
    video = scrapy.Field()
    # 视频格式没有
    # video_format = scrapy.Field()
    # 视频时长没有
    # duration = scrapy.Field()
    created_at = scrapy.Field()
    category = scrapy.Field()
    play_counts = scrapy.Field()
    like_counts = scrapy.Field()
    description = scrapy.Field()



# 作者信息
class ComposerItem(scrapy.Item):
    table_name = 'composers'
    cid = scrapy.Field()
    banner = scrapy.Field()
    avatar = scrapy.Field()
    # verified不知是什么
    # verified = scrapy.Field()

    name = scrapy.Field()
    intro = scrapy.Field()
    like_counts = scrapy.Field()
    fans_counts = scrapy.Field()
    follow_counts = scrapy.Field()
    location = scrapy.Field()
    career = scrapy.Field()



# 作者与视频关联信息
class CopyrightItem(scrapy.Item):
    table_name = 'copyrights'
    pcid = scrapy.Field()
    pid = scrapy.Field()
    cid = scrapy.Field()
    roles = scrapy.Field()


# 评论信息
class CommentItem(scrapy.Item):
    table_name = 'comments'
    commentid = scrapy.Field()
    pid = scrapy.Field()
    cid = scrapy.Field()
    avatar = scrapy.Field()
    uname = scrapy.Field()
    created_at = scrapy.Field()
    content = scrapy.Field()
    like_counts = scrapy.Field()
    reply = scrapy.Field()

