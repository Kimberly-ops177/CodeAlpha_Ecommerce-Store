from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Category, Product, Cart, CartItem, Order, OrderItem
from decimal import Decimal
import json

def home(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
        selected_category = get_object_or_404(Category, id=category_id)
    else:
        products = Product.objects.all()
        selected_category = None

    featured_products = Product.objects.filter(is_featured=True)[:4]

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'featured_products': featured_products,
    }
    return render(request, 'store/home.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    categories = Category.objects.all()
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related_products': related_products,
        'categories': categories
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def cart(request):
    cart_obj, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart_obj.items.all()
    total = cart_obj.get_total()
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_obj, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart_obj,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart!')

    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart')

@login_required
def checkout(request):
    cart_obj = get_object_or_404(Cart, user=request.user)
    cart_items = cart_obj.items.all()

    if not cart_items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart')

    total = cart_obj.get_total()

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        delivery_method = request.POST.get('delivery_method', 'doorstep')
        shipping_address = request.POST.get('shipping_address')

        order = Order.objects.create(
            user=request.user,
            customer_name=customer_name,
            customer_phone=customer_phone,
            total_amount=total,
            delivery_method=delivery_method,
            shipping_address=shipping_address
        )

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )

            cart_item.product.stock -= cart_item.quantity
            cart_item.product.save()

        cart_items.delete()

        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('order_detail', order_id=order.id)

    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def orders(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'store/orders.html', {'orders': user_orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_detail.html', {'order': order})

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def faqs(request):
    return render(request, 'store/faqs.html')
