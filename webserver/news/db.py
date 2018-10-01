#!/usr/bin/env python3

import pymongo
import datetime
import pprint
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
        if self.connection:
            self.connection.close()

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
