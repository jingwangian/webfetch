# -*- coding: utf-8 -*-
import scrapy
from webfetch.items import WebfetchItem
from scrapy.loader import ItemLoader
from scrapy.http import Request
from scrapy.loader.processors import MapCompose, Join
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from readability import Document


class BasicSpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['www.bbc.com']
    start_urls = ['https://www.bbc.com']
    # /world-asia-india-45636746',
    #               'https://www.bbc.com/news/technology-45674603']
    # 'https://www.bbc.com/news/entertainment-arts-45645653']
    # rules = (
    #     # Extract links matching 'category.php' (but not matching 'subsection.php')
    #     # and follow links from them (since no callback means follow=True by default).
    #     # Rule(LinkExtractor(allow=(r'news/world/asia',)), callback='parse_link'),
    #     # Rule(LinkExtractor(allow=(r'news/world/asia',))),

    #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    #     # Rule(LinkExtractor(allow=(r'news/world/asia', )), follow=True),
    #     Rule(LinkExtractor(allow=(r'news/', )), callback='parse_item'),
    # )

    rules = (
        Rule(LinkExtractor(allow=(r'news', r'sport'), restrict_xpaths=('//a[contains(@class,"media__link")]', '//a[contains(@class,"block-link__overlay-link")]')), callback='parse_item'),
        # Rule(LinkExtractor(allow=(r'news/'))),
    )

    def parse_item(self, response):
        # print("parse_item ----", response.url)

        item = WebfetchItem()
        doc = Document(response.text)
        item['title'] = doc.title()
        if item['title'].endswith("- BBC News"):
            item['title'] = item['title'][:-10].strip()

        item['title'] = item['title'].replace("/", "-")

        item['content'] = doc.summary()
        page_div = response.xpath('//*[@id="page"]/div')
        item['author'] = page_div.xpath('.//span[re:test(@class,"byline__name")]/text()').extract()
        # item['author'] = response.xpath('//*[@id="page"]/div/div/div/div/div/div/div/a/span[@class="byline__name"]/text()').extract()
        item['url'] = response.url

        return item

    def parse_link(self, response):
        print("parse_link ----", response.url)
