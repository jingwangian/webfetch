# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


def strip_fun(x):
    return x.strip()


class WebfetchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    title = Field()
    author = Field()
    content = Field()
    post_date = Field()

    # Housekeeping fields
    # project = Field()
    # spider = Field()
    # server = Field()
    # date = Field()
