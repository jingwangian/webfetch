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
    name = 'basic'
    allowed_domains = ['www.bbc.com']
    start_urls = ['https://www.bbc.com/news/world-45638201']

    def parse(self, response):
        # print("parse_item ----", response.url)

        # if response.url.endswith("news/world/asia"):
        #     print("parse_item ---- endswith news/world/asia")
        #     yield Request(response.url)

        # links = LinkExtractor(allow=('news', 'sport'), restrict_xpaths=('//a[contains(@class,"media__link")]', '//a[contains(@class,"block-link__overlay-link")]')).extract_links(response)

        # [print(url.url) for url in links]

        # c = response.xpath('//*[@id="page"]/li')

        # uls = response.xpath('//*[@id="page"]/section/div/ul/')
        # for u in uls:
        # links = response.xpath('//li[contains(@class,"media-list__item")]//a[contains(@class,"media__link") or contains(@class,"block-link__overlay-link")]')
        # # [print(c) for c in links]
        # for l in links:
        #     print(l)
        #     print(l.xpath('@href').extract())

        # return

        item = WebfetchItem()
        doc = Document(response.text)
        item['title'] = doc.title()
        item['content'] = doc.summary()
        page_div = response.xpath('//*[@id="page"]/div')
        item['author'] = page_div.xpath('.//span[re:test(@class,"byline__name")]/text()').extract()
        # item['author'] = response.xpath('//*[@id="page"]/div/div/div/div/div/div/div/a/span[@class="byline__name"]/text()').extract()
        item['url'] = response.url
        print("url ----", item['url'])
        print("title ---- ", item['title'])
        print("author ---- ", item['author'])
        print("content ----", item['content'])

        print('')

        return item

    def parse_link(self, response):
        print("parse_link ----", response.url)
