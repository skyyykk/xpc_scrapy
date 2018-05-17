import random
from scrapy.exceptions import NotConfigured


class RandomProxyMiddleware(object):
    def __init__(self,settings):
        self.proxies = settings.getlist('PROXIES')
        self.stats = {}.fromkeys(self.proxies,0)
        self.max_failed = 2
    @classmethod
    def from_crawler(cls,crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        return cls(crawler.settings)

    def process_request(self,request,spider):
        if not 'proxy' in request.meta:
            request.meta['proxy'] = random.choice(self.proxies)
            print('-'*50,request.meta['proxy'])

    def process_response(self,request,response,spider):
        cur_proxy = request.meta['proxy']
        if response.status >= 400:
            self.stats[cur_proxy] += 1
        if self.stats[cur_proxy] >= self.max_failed:
            if cur_proxy in self.proxies:
                self.proxies.remove(cur_proxy)
                print('del %s from proxies list' % cur_proxy)
        return response

    def process_exception(self,request,exception,spider):
        cur_proxy = request.meta['proxy']
        print('raise exception:%s when use %s.' %
              (exception, cur_proxy))
        if cur_proxy in self.proxies:
            self.proxies.remove(cur_proxy)
            print('del %s from proxies list' % cur_proxy)











