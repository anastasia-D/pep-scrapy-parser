import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (
    PEP_ALLOWED_DOMAINS,
    PEP_INDEX_URL,
    PEP_SPIDER_NAME,
)

PEP_HEADING = re.compile(r'PEP\s+(\d+)\s+[–—-]\s+(.+)')


class PepSpider(scrapy.Spider):
    name = PEP_SPIDER_NAME
    allowed_domains = [PEP_ALLOWED_DOMAINS]
    start_urls = [PEP_INDEX_URL]

    def parse(self, response):
        links = response.css(
            'table.pep-zero-table tr > td:nth-child(2) > a.pep::attr(href)'
        ).getall()
        if not links:
            self.logger.error('В числовом индексе не найдены ссылки на PEP')
            return
        yield from response.follow_all(links, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title').xpath('normalize-space(.)').get()
        heading = PEP_HEADING.fullmatch(title or '')
        status = response.css('#pep-page-section').xpath(
            './/dt[normalize-space(.) = "Status:" or normalize-space(.) = '
            '"Status"]/following-sibling::*[1][self::dd]'
        ).xpath('normalize-space(.)').get()
        if not heading or not status:
            self.logger.warning('Пропущен PEP с неполными полями: %s', response.url)
            self.crawler.stats.inc_value('pep/incomplete_pages')
            return
        number, name = heading.groups()
        yield PepParseItem(number=number, name=name, status=status)
