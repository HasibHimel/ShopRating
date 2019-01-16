from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
    path('<int:shoppingmall_id>/', views.detail_mall, name='detail_mall'),
    path('<int:shoppingmall_id>/', views.detail_shop(), name='detail_shop'),
    path('<int:shoppingmall_id>/', views.detail_mall, name='detail_mall')
]