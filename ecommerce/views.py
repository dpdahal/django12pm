from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomerForm
from django.contrib.auth.models import User
from cart.cart import Cart


# Create your views here.

def index(request):
    data = {
        'bannerData': Banner.objects.filter(is_active=True),
        'productsData': Product.objects.order_by('-id'),
    }
    return render(request, 'frontend/pages/index/index.html', data)


def contact(request):
    return render(request, 'frontend/pages/contact/contact.html')


def product_list(request):
    productData = Product.objects.order_by('-id')
    paginator = Paginator(productData, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'productsData': page_obj,
    }
    return render(request, 'frontend/pages/product/product.html', data)


def product_details(request, slug):
    productData = Product.objects.get(slug=slug)
    categoryId = productData.category_id
    relatedData = Product.objects.filter(category_id=categoryId)
    data = {
        'productData': productData,
        'relatedData': relatedData,
    }
    return render(request, 'frontend/pages/product/details.html', data)


def product_category(request, slug):
    categoryData = Category.objects.get(slug=slug)
    productsData = Product.objects.filter(category_id=categoryData.id)
    data = {
        'productsData': productsData,
    }
    return render(request, 'frontend/pages/product/category.html', data)


def product_search(request):
    if request.method == "POST":
        criteria = request.POST['criteria']
        productsData = Product.objects.filter(Q(name__icontains=criteria) | Q(description__icontains=criteria))
        paginator = Paginator(productsData, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'productsData': page_obj,
        }

        return render(request, 'frontend/pages/product/product.html', data)

    else:
        return redirect('product')


def custom_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        user = User.objects.create_user(username=username, email=email, password=password)
        Customer.objects.create(user=user, phone=phone, address=address, city=city)
        messages.success(request, 'Registration successful')
        return redirect('login')

    else:
        data = {
            'form': CustomerForm(),
        }
        return render(request, 'frontend/pages/register/register.html', data)


def custom_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            back = request.META.get('HTTP_REFERER')
            return redirect(back)
    else:
        data = {
            'form': AuthenticationForm(),
        }
        return render(request, 'frontend/pages/login/login.html', data)


def custom_logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def user_dashboard(request):
    return render(request, 'frontend/pages/user/dashboard.html')


@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'frontend/pages/cart/cart_detail.html')
