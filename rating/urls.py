from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:mall_id>/mall/', views.shop, name='shop'),
    path('<int:shop_id>/shop/', views.product, name='product'),
    path('<int:product_id>/product/', views.detail, name='detail'),
    path('<int:mall_id>/rate_mall/', views.rate_mall, name='rate_mall'),
    path('<int:shop_id>/rate_shop/', views.rate_shop, name='rate_shop'),
    path('<int:product_id>/rate_product/', views.rate_product, name='rate_product'),
]