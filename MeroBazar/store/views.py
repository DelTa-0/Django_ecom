from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{
        'product':product
    })

def category(request,cat):
    #Replace space with - to solve url issue EG smart watch has space it will be smart-watch
    cat=cat.replace('-',' ')
    try:
        category=Category.objects.get(name=cat)
        products=Product.objects.filter(category=category)
        return render(request,'category.html',{
            'products':products,
            'category':category
        })
    except:
        messages.success(request,("category doesnot exist!!"))
        return redirect('home')


def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{
        'products':products
    })

def about(request):
    return render(request,'about.html')


def register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("you have registered!!"))
            return redirect('home')
        else:
            messages.success(request,("Cannot register try again"))
            return redirect('register')
    else:
        return render(request,'register.html',{
            'form':form
        })
    

def login_user(request):
    if request.method=='POST':
        print(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,("you have logged in!"))
            return redirect('home')
        else:
            messages.success(request,("there was error. Try again!!"))
            return redirect('login')
    else:
        
        return render(request,'login.html')
    

    

def logout_user(request):
    logout(request)
    messages.success(request,("you have successfully logged out!"))
    return redirect('home')