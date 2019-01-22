from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse

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
        raise Http404("Shop does not exist")
    return render(request, 'rating/product.html', {'shopp': shopp})


def detail(request, product_id):
    try:
        productt = Product.objects.get(pk=product_id)
    except Product.DoesNotExit:
        raise Http404("Product does not exist")
    return render(request, 'rating/detail.html', {'productt': productt})


def rate_mall(request, mall_id):
    mall = get_object_or_404(Mall, pk=mall_id)
    divisor = mall.rate_counter
    total_rating = mall.mall_rating * divisor
    rating = request.POST['rate_mall']
    new_total_rating = total_rating + float(rating)
    new_rating = new_total_rating/(divisor+1)
    mall.rate_counter += 1
    mall.mall_rating = new_rating
    mall.save()

    return HttpResponseRedirect(reverse('shop', args=(mall.id,)))


def rate_shop(request, shop_id):
    shopp = get_object_or_404(Shop, pk=shop_id)
    divisor = shopp.rate_counter
    total_rating = shopp.shop_rating * divisor
    rating = request.POST['rate_shop']
    new_total_rating = total_rating + float(rating)
    new_rating = new_total_rating/(divisor+1)
    shopp.rate_counter += 1
    shopp.shop_rating = new_rating
    shopp.save()

    return HttpResponseRedirect(reverse('product', args=(shopp.id,)))


def rate_product(request, product_id):

    productt = get_object_or_404(Product, pk=product_id)
    rating = float(request.POST['rate_product'])

    divisor = productt.rate_counter
    total_rating = productt.product_rating * divisor
    new_total_rating = total_rating + rating
    new_rating = new_total_rating/(divisor+1)
    productt.rate_counter += 1
    productt.product_rating = new_rating
    productt.save()

    return HttpResponseRedirect(reverse('detail', args=(productt.id,)))






