#!/usr/bin/env python3

import os
import pymongo
import datetime
import pprint
import argparse
from pymongo import MongoClient


class MongoDBAgent:
    def __init__(self, host="localhost", port=27017, username="root", password="example"):
        self.host = host or "localhost"
        self.port = port or 27017
        self.username = username
        self.password = password

        self.connection = None

        # self.connect()

    def __del__(self):
        if self.connection:
            self.connection.close()
        # pass

    def connect(self):
        self.connection = MongoClient(host=self.host,
                                      port=self.port,
                                      username=self.username,
                                      password=self.password)
        # print(self.connection)
        # print(dir(self.connection))
        self.db = self.connection.newsdb
        self.tb_news = self.db.news

        self.tb_news.create_index([("content", 'text')], unique=True)

        return self.connection

    def insert(self, data: dict):
        """
        """
        self.tb_news.insert_one(data)

    def insert_many(self, data_list: list):
        self.tb_news.insert_many(data_list)

    def search(self):
        pass

    def text_search(self, text):
        return self.tb_news.find({"$text": {"$search": text}})

    def delete_all(self) -> int:
        x = self.tb_news.delete_many({})

        return x.deleted_count

    def find_one(self, field, text):
        return self.tb_news.find_one({field: text})

    def find_all(self):
        cursor = self.tb_news.find()
        for c in cursor:
            yield c


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd',
                        help='command:[del-all, search, url]')
    parser.add_argument('--text',
                        help='searched text')

    parser.add_argument('--url',
                        help='searched url')
    args = parser.parse_args()

    opt_cmd = args.cmd
    text = args.text
    url = args.url

    mongodb_host = os.getenv("MONGODB_HOST", "localhost")
    dba = MongoDBAgent(host=mongodb_host)
    dba.connect()

    if opt_cmd == "del-all":
        dba.delete_all()
    elif opt_cmd == "search":
        cursor = dba.text_search(text)

        for x in cursor:
            print("{} : {}".format(x["url"], x["title"]))
    elif opt_cmd == "url":
        result = dba.find_one("url", url)
        print(result["url"])
        print(result["content"])


if __name__ == '__main__':
    main()
