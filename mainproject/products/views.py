from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

from django.views.generic import ListView
# Create your views here.

def index(request):
    return render(request,'products_app/index.html')

class ProductView(ListView):
    model = Product
    template_name = 'products_app/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['categories'] = Category.objects.all()
        # context['subcategories'] = SubCategory.objects.all()
        # context['brends'] = Brends.objects.all()        
        return context

def ProductListView(request,id):
    query = Product.objects.filter(category=id)
    print(query,id)
    return render(request,'products_app/goods_list.html',context={
        'product_lists': query
    })

def ProductDetail(request,id):
  

    query = get_object_or_404(Product,id=id)
    print('queryyyyyyyyyyyyyyyyyy',query)
    return render(request,'products_app/product-details.html',context={
        'product_details': query
        })
   
    


    
    
# class ProductListView(ListView):
#     model  = Product      
#     template_name = 'products_app/goods_list.html'
#     context_object_name = 'product_lists'

#     def get_queryset(self,id):

#         return Product.objects.filter(id=id)
    


