from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('markets/', views.markets, name='markets'),
    path('markets/<slug:slug>/', views.markets_detail, name='market_detail_slug'),
    path('products/<slug:slug>/<int:product_id>/', views.product_detail, name='product_detail'),
]