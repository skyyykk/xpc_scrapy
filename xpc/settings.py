# -*- coding: utf-8 -*-

# Scrapy settings for xpc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xpc'

SPIDER_MODULES = ['xpc.spiders']
NEWSPIDER_MODULE = 'xpc.spiders'
# -o 文件输出直接显示为中文
FEED_EXPORT_ENCODING = 'utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# ITEM_PIPELINES={
#     'scrapy_redis.pipeline.RedisPipeline'
# }
REDIS_URL = 'redis://@10.36.135.98:6379'
SCHEDULER_PERSIST = True
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_TIMEOUT = 5
# 是否使用代理
HTTPPROXY_ENABLED = True
PROXIES = ['http://123.206.133.179:1704',
           'http://39.106.202.68:1704',
           'http://120.79.56.156:1704',
           'http://39.106.57.53:1704',
           'http://47.93.203.231:1704',
           'http://140.143.141.236:1704',
           'http://120.78.162.253:1704',
           'http://39.107.96.88:1704',
           'http://39.107.98.78:1704',
           'http://203.195.230.40:1704',
           'http://47.106.117.214:1704',
           'http://39.105.102.177:1704',
           'http://140.143.155.139:1704',
           'http://39.108.3.52:1704',
           'http://47.95.13.99:1704',
           'http://39.104.112.68:1704',
           'http://112.74.172.140:1704',
           'http://112.74.57.120:1704',
           'http://39.108.139.176:1704',
           'http://203.195.204.174:1704',
           'http://47.95.195.216:1704',
           'http://139.199.68.216:1704',
           'http://39.106.57.137:1704',
           'http://39.105.80.9:1704',
           'http://59.110.219.8:1704',
           'http://211.159.147.237:1704',
           'http://39.108.8.146:1704',
           ]
# 并发请求的数量
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载延迟时间
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:

# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# cookies的自动保存和使用
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Cookie': "Device_ID=5af3e2e1857ee; Authorization=37E86478630B2165C630B24EB2630B283B9630B2E5167452D716; _ga=GA1.2.897450412.1525932769; zg_did=%7B%22did%22%3A%20%2216348ae544c2f3-07669e61acba54-454c092b-1fa400-16348ae544d212%22%7D; UM_distinctid=16348ae557d2df-0db3e965e142ea-454c092b-1fa400-16348ae557e283; bdshare_firstime=1525932787821; Hm_lvt_dfbb354a7c147964edec94b42797c7ac=1525932773,1526003484; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216348ae6c4b22b-0e3b3095b12003-454c092b-2073600-16348ae6c4c3ae%22%2C%22%24device_id%22%3A%2216348ae6c4b22b-0e3b3095b12003-454c092b-2073600-16348ae6c4c3ae%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; CNZZDATA1262268826=1630873441-1525929423-http%253A%252F%252Fwww.xinpianchang.com%252F%7C1526017022; zg_c9c6d79f996741ee958c338e28f881d0=%7B%22sid%22%3A%201526016664.68%2C%22updated%22%3A%201526017285.541%2C%22info%22%3A%201525932774484%7D; cn_1262268826_dplus=%7B%22distinct_id%22%3A%20%2216348ae557d2df-0db3e965e142ea-454c092b-1fa400-16348ae557e283%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201526020170%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201526020170%7D%7D; PHPSESSID=egu56smj3plo5drohq1ql0oj40; _gid=GA1.2.789015899.1526282876; _gat=1",
    'Host': "www.xinpianchang.com",
    'Upgrade-Insecure-Requests': "1",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xpc.middlewares.XpcSpiderMiddleware': 749,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'xpc.middlewares.RandomProxyMiddleware': 749,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xpc.pipelines.XpcPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
