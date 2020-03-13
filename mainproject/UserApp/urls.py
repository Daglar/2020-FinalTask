from django.urls import path 
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'UserApp'

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',CustomRegisterView.as_view(),name='register'),
    path('reset-password/',CustomResetView.as_view(),name='reset-password'),
    path('user-register/', CustomUserregisterView.as_view(),name='user-register'),
    
]