from django.urls import path 
from .views import *

app_name = 'products'

urlpatterns = [
    path('',ProductView.as_view(),name='product'),
    path('cat/<int:id>/',ProductListView,name='productlist'),
    path('product/detail/<int:id>/',ProductDetail,name='productdetail')
]
