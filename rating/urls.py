from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:mall_id>/mall/', views.shop, name='shop'),
    path('<int:shop_id>/shop/', views.product, name='product'),
    path('<int:product_id>/product/', views.detail, name='detail'),
]