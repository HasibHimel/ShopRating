from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Mall, Shop, Product


def index(request):
    mall_list = Mall.objects.all()
    #template = loader.get_template('rating/index.html')
    context ={
        'mall_list': mall_list,
    }
    return render(request, 'rating/index.html', context)


def shop(request, mall_id):
    try:
        mall = Mall.objects.get(pk=mall_id)
    except Mall.DoesNotExist:
        raise Http404("Mall does not exit")
    return render(request, 'rating/shop.html', {'mall': mall})


def product(request, shop_id):
    try:
        shopp = Shop.objects.get(pk=shop_id)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exit")
    return render(request, 'rating/product.html', {'shopp': shopp})


