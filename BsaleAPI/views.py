from django.db.models import query
from django.shortcuts import render
from django.views import View
from .models import Category, Product
from django.http import JsonResponse


class CategoryView(View):
    def get(self, request):
        queryset = Category.objects.all()
        return JsonResponse(list(queryset.values()), safe=False)

class ProductView(View):
    def get(self, request):
        queryset = Product.objects.all()
        categoryFilter = self.request.GET.get('category', None)
        productFilter = self.request.GET.get('product_name', None)

        if categoryFilter is not None and productFilter is not None:
            queryset = queryset.filter(category=categoryFilter,name__icontains=productFilter)


        if categoryFilter is not None:
            queryset = queryset.filter(category=categoryFilter)


        if productFilter is not None:
            queryset = queryset.filter(name__icontains=productFilter)


        return JsonResponse(list(queryset.values()), safe=False)

        
        

        

        
       
       

        



