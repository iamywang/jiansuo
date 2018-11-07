from django.shortcuts import render
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import socket


def index(request):
    result_list = []
    if request.method == "POST":
        str = request.POST.get("str", None)
        print("被查询：" + str+"：--ALL")
        result_list = search(str)
    return render(request, "../templates/index.html", {"data": result_list})


def qq(request):
    result_list = []
    if request.method == "POST":
        str = request.POST.get("str", None)
        print("被查询：" + str+"：--QQ")
        result_list = search_qq(str)
    return render(request, "../templates/qq.html", {"data": result_list})


def qqqun(request):
    result_list = []
    if request.method == "POST":
        str = request.POST.get("str", None)
        print("被查询：" + str+"：--Qun")
        result_list = search_qun(str)
    return render(request, "../templates/qqqun.html", {"data": result_list})


def wy_163(request):
    result_list = []
    if request.method == "POST":
        str = request.POST.get("str", None)
        print("被查询：" + str+"：--163")
        result_list = search_163(str)
    return render(request, "../templates/163.html", {"data": result_list})


def search(key_word):
    result_list = []
    my_index = open_dir("sgk/all", indexname='list')
    with my_index.searcher() as searcher:
        parser = QueryParser("line", my_index.schema)
        my_query = parser.parse(key_word)
        results = searcher.search(my_query, limit=None)
        count = 0
        for result_item in results:
            count = count + 1
            result_item = dict(result_item)
            result_item["num"] = count
            result_list.append(result_item)
    return result_list


def search_163(key_word):
    result_list = []
    my_index = open_dir("sgk/163", indexname='163')
    with my_index.searcher() as searcher:
        parser = QueryParser("Email", my_index.schema)
        my_query = parser.parse(key_word)
        results = searcher.search(my_query, limit=None)
        count = 0
        for result_item in results:
            count = count + 1
            result_item = dict(result_item)
            result_item["num"] = count
            result_list.append(result_item)
    return result_list


def search_qq(key_word):
    result_list = []
    my_index = open_dir("sgk/QQ", indexname='qqq')
    with my_index.searcher() as searcher:
        parser = QueryParser("Nick", my_index.schema)
        my_query = parser.parse(key_word)
        results = searcher.search(my_query, limit=None)
        count = 0
        for result_item in results:
            count = count + 1
            result_item = dict(result_item)
            result_item["num"] = count
            result_list.append(result_item)
    return result_list


def search_qun(key_word):
    result_list = []
    my_index = open_dir("sgk/QQqun", indexname='list')
    with my_index.searcher() as searcher:
        parser = QueryParser("Title", my_index.schema)
        my_query = parser.parse(key_word)
        results = searcher.search(my_query, limit=None)
        count = 0
        for result_item in results:
            count = count + 1
            result_item = dict(result_item)
            result_item["num"] = count
            result_list.append(result_item)
    return result_list
