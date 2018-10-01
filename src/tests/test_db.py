#!/usr/bin/env python3
import pytest
from webfetch.db import MongoDBAgent
from datetime import datetime


@pytest.fixture
def db_client():

    dba = MongoDBAgent()
    dba.connect()

    return dba


class TestMongoDBAgent:
    def test_init(self):
        dba = MongoDBAgent()

        assert dba.username == 'root'

    def test_connect(self):

        db_client = MongoDBAgent()
        c = db_client.connect()

        print(c)

    def test_insert(self, db_client):
        db_client.delete_all()
        data = {
            "url": "http://a/b/c",
            "title": "tt1",
            "content": "This is a very good news.",
            "author": "John smith",
            "post_date": "2018-01-02",
            "created_date": datetime.utcnow().isoformat()
        }
        db_client.insert(data)
        result = db_client.find_one("title", "tt1")

        db_client.delete_all()
        assert result == data

    def test_text_search(self, db_client):
        db_client.delete_all()
        data = [{
            "url": "http://a/b/c",
            "title": "tt1",
            "content": "This is a very good news.",
            "author": "John smith",
            "post_date": "2018-01-02",
            "created_date": datetime.utcnow().isoformat()
        },
            {
            "url": "http://a/b/d",
            "title": "tt2",
            "content": "This is a bad news today",
            "author": "John will",
            "post_date": "2018-01-03",
            "created_date": datetime.utcnow().isoformat()
        }
        ]

        db_client.insert_many(data)
        c = db_client.text_search("today")

        for x in c:
            assert x == data[1]

        # assert

    def test_find_all(self, db_client):
        db_client.delete_all()
        data = [{
            "url": "http://a/b/c",
            "title": "tt1",
            "content": "This is a very good news.",
            "author": "John smith",
            "post_date": "2018-01-02",
            "created_date": datetime.utcnow().isoformat()
        },
            {
            "url": "http://a/b/d",
            "title": "tt2",
            "content": "This is a bad news today",
            "author": "John will",
            "post_date": "2018-01-03",
            "created_date": datetime.utcnow().isoformat()
        }
        ]

        db_client.insert_many(data)

        for x in db_client.find_all():
            assert x in data

        # assert 0
