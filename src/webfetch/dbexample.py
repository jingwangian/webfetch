#!/usr/bin/env python3

import pymongo
import datetime
import pprint

from pymongo import MongoClient
myclient = pymongo.MongoClient(host='localhost', port=27017, username="root", password="example")

mydb = myclient.mydatabase

print(myclient.list_database_names())

posts = mydb.posts

# posts.create_index([("text", 'text')], unique=True)

# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
# new_posts = [{"author": "Mike",
#               "text": "Another post!",
#               "tags": ["bulk", "insert"],
#               "date": datetime.datetime(2009, 11, 12, 11, 14)},
#              {"author": "Eliot",
#               "title": "MongoDB is fun",
#               "text": "and pretty easy too!",
#               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
# post_id = posts.insert_one(post).inserted_id
# result = posts.insert_many(new_posts)

# print(result.inserted_ids)
# print(post_id)
# ret = posts.find_one()
# pprint.pprint(ret)
# print(type(ret))


# for post in posts.find():
#     pprint.pprint(post)

# cursor = posts.find({"author": "Mike", "tags": {"$in": ["insert","python"]}})
cursor = posts.find({
    # "author": "Mike",
    "$text": {"$search": "first post"}
})
print(type(cursor))


for t in cursor:
    pprint.pprint(t)

cursor.close()
# pprint(ret.g)
# print(type(posts))
