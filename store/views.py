from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    products = Product.objects.all()
    items = len(Order.objects.all())
    context = {'products':products, 'items':items} 
    return render(request,'store/home.html', context)

def detailView(request, name):
    product = get_object_or_404(Product, name=name)

    context = {'product':product}
    return render(request,'store/detail.html', context)

def SignUpView(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    
    context = {'form':form}
    return render(request,'store/signup.html',context)

def loginView(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')            
    else:
        form = AuthenticationForm()

    context = {'form':form}
    return render(request,'store/login.html', context)
    
def logoutView(request):
    logout(request)
    return redirect('login')

def orderView(request):
    orders = Order.objects.all()
    sum_items = sum([order.quantity for order in orders])
    sum_price = sum([order.total_sum for order in orders])
    context = {'orders':orders,'sum_items':sum_items,'sum_price':sum_price}
    return render(request,'store/order.html', context)

def add_order(request,name):
    product = Product.objects.get(name=name)
    try:
        order = Order.objects.get(product=product)
    except:
        order = Order.objects.create(product=product)
        order.save()
    
    try:
        order.quantity+=1
        order.save()
        print(order.quantity)
    except:
        print("Error")
        
    return redirect('order')

def addQuantityView(request, name):
    product = Product.objects.get(name=name)
    order = Order.objects.get(product=product)
    try:
        order.quantity+=1
        order.save()
    except:
        print("Error")

    return redirect('order')

def lessQuantityView(request, name):
    product = Product.objects.get(name=name)
    order = Order.objects.get(product=product)
    try:
        order.quantity-=1
        order.save()
    except:
        print("Error")

    return redirect('order')

def checkoutView(request):
    orders = Order.objects.all()
    sum_items = sum([order.quantity for order in orders])
    sum_price = sum([order.total_sum for order in orders])
    context = {'orders':orders,'sum_items':sum_items,'sum_price':sum_price}
    return render(request,'store/checkout.html', context)

