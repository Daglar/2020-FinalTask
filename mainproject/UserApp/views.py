from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, PasswordResetView
from .forms import CustomRegisterForm,CustomLoginForm, ResetPasswordForm,CustomUserRegistrationForm
from django.contrib.auth import get_user_model


User = get_user_model

# Create your views here.

# def login(request):
#     return render(request,'UserApp/login.html')

   



class CustomRegisterView(CreateView):
    model = User
    template_name = 'UserApp/register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('UserApp:login')

    # def post(self, request):
    #     print(request.POST)
    #     return super().post(request)

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     return super().post(request, *args, **kwargs)    

    # {% comment %} 
	# 		    $('#registerform').submit(function(e){
	# 		 	e.preventDefault()
	# 		 	var eded=$("#operators").val()
	# 		 	var mobile=$("#mobile").val()
	# 		 	alert(eded+mobile)
	# 		 	$.ajax({
			
	# 		 		url:'{% url "UserApp:register" %}',
	# 		 		method:'GET',
	# 		 		data:{''}
	# 		 	})
	# 		   }) {% endcomment %}


class CustomLoginView(LoginView):
    template_name = 'UserApp/login.html'
    form_class = CustomLoginForm  
    

class CustomResetView(PasswordResetView):
    template_name = 'UserApp/reset-password.html'  
    form_class = ResetPasswordForm
    success_url = reverse_lazy('UserApp:login')

class CustomUserregisterView(CreateView):
    template_name = 'UserApp/user-register.html' 
    form_class = CustomUserRegistrationForm 
    success_url = reverse_lazy('UserApp:login')
 


