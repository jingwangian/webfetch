Introduction
============
This is a small system to crawl data from https://www.bbc.com and save them into
MongoDB.
A simple webserver is used to provide the RESTAPI to visit the downloaded data.

Requirement
===========
docker and docker-compose is needed before build the system

Build the system
================
run 'make' to build the docker file and get the docker images
run docker-compose up -d to start the services

Docker Services
===============
fetcher: Is used to crawl the data from https://www.bbc.com and save it into MongoDB
MongoDB: A NoSQL database
web: A webserver used to provide the RESTFul API
mongo-express: A service used to visit the MongoDB directly

Start the system
================
docker-compose up -d

Check the running service
=========================
docker-compose ps

crawl data
==========
If you want to crawl data again, Use the command : ./fetch.sh
It will crawl the data from https://www.bbc.com and save it into the MongoDB

Restful api
===========

Action         URL                    Description
--------------------------------------------------------------------
GET         /news/list               list all data
GET         /news/search/<key>       search data, <key> is the words
                                     to be searched in the articles
GET         /news/rm                 remove all existing data

host address: http://127.0.0.1:8000

