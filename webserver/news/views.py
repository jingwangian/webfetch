from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from webserver.settings import MONGODB_HOST
from . import db
# Create your views here.
# import os


print("MONGODB_HOST is", MONGODB_HOST)
dba = db.MongoDBAgent(host=MONGODB_HOST)


def index(request):
    context = {}

    # print("current path:", os.getcwd())
    # chatrobot.reset()

    # dba.connect()

    # content_list = [x["content"] for x in dba.find_all()]

    # context = {
    #     "contents": content_list,
    # }

    return HttpResponse("This is an index page for news")

    # return render(request, 'news/basic.html', context)


def list(request):
    dba.connect()
    res_message = dict()

    content_list = []
    for x in dba.find_all():
        x.pop("_id")
        x.pop("content")
        content_list.append(x)

    res_message['contents'] = content_list

    return JsonResponse(content_list, safe=False)


def rm(request):
    """Remove all content from db
    """
    dba.connect()
    number = dba.delete_all()

    return HttpResponse("Total {} records have been deleted!".format(number))


def search_news(request, message):
    print("Input message: ", message)

    dba.connect()
    res_message = dict()
    content_list = []
    cursor = dba.text_search(message)
    for x in cursor:
        x.pop("_id")
        x.pop("content")
        print("Find url:", x["url"])
        content_list.append(x)

    res_message['contents'] = content_list

    return JsonResponse(content_list, safe=False)
