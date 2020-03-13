from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, CustomUserRegistration
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,PasswordResetForm 

OPERATORS =( 
    ("050", "050"), 
    ("051", "051"), 
    ("055", "055"), 
    ("070", "070"), 
    ("077", "077"),
    ("099", "099"),
)

class CustomRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
                # 'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Username'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
                'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
                # 'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Surname'
    }))
    # operators = forms.ChoiceField(choices = OPERATORS) 

    mobile = forms.CharField(widget=forms.TextInput(attrs={
                # 'unique' : True,
                # 'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Telephone Number',
                'type' : "hidden",
                'id' : 'mobile'
                
    }))    
  
    email = forms.CharField(widget=forms.EmailInput(attrs={
                # 'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                # 'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                # 'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Confirm password'
    }))
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'username', 'mobile','email','password1','password2']   

    
    
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder' : ' Username'
    }))
    password = forms.CharField(label='',strip=False,widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Password'
    }))    

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }), max_length=254)         

class CustomUserRegistrationForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder' : ' Name'
    }))
    shop_name = forms.CharField(label='',strip=False,widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Shop name'
    }))    
    # shop_link = forms.CharField(label='',strip=False,widget=forms.TextInput(attrs={
    #             'class': 'form-control',
    #             'placeholder' : "Shop's website (not important)",
                

    # }))    

    class Meta:
        model = CustomUserRegistration
        fields = ['name', 'shop_name']   