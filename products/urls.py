from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    OrderItemDetailView, OrderItemListCreateView,
    CategoryDetailView, CategoryListCreateView,
    OrderListCreateView, OrderDetailView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('orderitems/', OrderItemListCreateView.as_view(), name='orderitem-list'),
    path('orderitems/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),
    path('category/', CategoryListCreateView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
