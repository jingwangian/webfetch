# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

from scrapy.http.response.html import HtmlResponse
from webfetch.db import MongoDBAgent

mongodb_host = os.getenv("MONGODB_HOST", "localhost")
dba = MongoDBAgent(host=mongodb_host)
dba.connect()


class WebfetchPipeline(object):
    def process_item(self, item, spider):
        # print("process_item:", item)

        # file_path = "downloads"
        # file_name = '-'.join([x.strip() for x in item['title'].split(' ')])

        # file_name = file_name + '.html'

        # full_file_name = os.path.join(file_path, file_name)

        print("url ----", item['url'])
        print("title ---- ", item['title'])
        print("author ---- ", item['author'])
        print("content length ---- ", len(item['content']))

        # with open(full_file_name, 'w') as wf:
        #     # wf.write("title :".format(item['title']))
        #     if len(item['content']) > 500:
        #         wf.write(item['content'])

        # print(dict(item))
        if len(item['content']) > 500:
            url = item["url"]
            if dba.find_one("url", url):
                print("{} is already exist".format(url))
            else:
                dba.insert(dict(item))

        print('')
        return item

    def get_plain_text(self, url, content):
        response = HtmlResponse(url=url, body=content)

        p_list = response.xpath('//p')

        text = ''

        text_list = []
        for p in p_list:
            try:
                t = p.xpath("text()").extract_first()
                # print("t---:", t)
                if t:
                    text_list.append(t.lower().strip())
            except TypeError:
                print("TypeError")

        text = ' '.join(text_list)

        # print("total:", text)

        return text
