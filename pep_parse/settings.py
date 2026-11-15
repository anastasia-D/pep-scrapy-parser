BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS_PER_DOMAIN = 4
DOWNLOAD_DELAY = 0.25
DOWNLOAD_TIMEOUT = 30

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEED_EXPORT_ENCODING = 'utf-8'
FEEDS = {
    'results/pep_%(batch_time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'mode': 'create',
        'store_empty': False,
    },
}

PEP_SPIDER_NAME = 'pep'
PEP_ALLOWED_DOMAINS = 'peps.python.org'
PEP_INDEX_URL = 'https://peps.python.org/numerical/'
