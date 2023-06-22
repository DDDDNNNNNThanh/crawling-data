BOT_NAME = 'data_price'

SPIDER_MODULES = ['data_price.spiders']
NEWSPIDER_MODULE = 'data_price.spiders'

ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
}

FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,  
    'data_price.middlewares.DataPriceDownloaderMiddleware': 543,
}
