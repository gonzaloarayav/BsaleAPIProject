from django.urls import path
from .views import CategoryView, ProductView

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category_list'),
    path('product/', ProductView.as_view(), name='product_list')
]