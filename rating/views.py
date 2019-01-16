from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


def detail_mall(request, shoppingmall_mall_name):
    return HttpResponse("%s." % shoppingmall_mall_name)


def detail_shop(request, shop_shop_name):
    return HttpResponse("%s." % shop_shop_name)


def rate_mall(request, shoppingmall_id):
    return HttpResponse("Rate for %s." % shoppingmall_id)


def rate_shop(request, shop_id):
    return HttpResponse("Rate for %s." % shop_id)


def rate_product(request, product_id):
    return HttpResponse("Rate for %s." % product_id)

