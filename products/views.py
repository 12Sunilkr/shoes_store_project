from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from .models import Category, Product, Order
import json


def home(request):
    categories = Category.objects.all()[:4]  # Get first 4 categories
    trending_products = Product.objects.filter(stock__gt=0).order_by('-created_at')[:8]  # Get 8 newest products
    
    # Get 3-4 featured products for carousel
    featured_products = Product.objects.filter(stock__gt=0).order_by('?')[:4]
    
    context = {
        'categories': categories,
        'trending_products': trending_products,
        'featured_products': featured_products,
    }
    return render(request, 'home.html', context)


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/product_list.html', context)


def search_products(request):
    query = request.GET.get('q', '')
    products = []
    
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    
    context = {
        'query': query,
        'products': products,
        'categories': Category.objects.all(),
    }
    return render(request, 'products/search_results.html', context)


def cart(request):
    cart_items = []
    total = 0
    count = 0
    
    if 'cart' in request.session:
        for item_id, item_data in request.session['cart'].items():
            product = get_object_or_404(Product, id=int(item_id))
            quantity = int(item_data['quantity'])
            subtotal = product.price * quantity
            total += subtotal
            count += quantity
            
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })
    
    recommended_products = Product.objects.filter(stock__gt=0).order_by('?')[:4]
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'count': count,
        'recommended_products': recommended_products,
    }
    return render(request, 'products/cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0 or quantity > product.stock:
        messages.error(request, f'Please select a quantity between 1 and {product.stock}')
        return redirect('product_detail', pk=product_id)
    
    # Initialize cart if it doesn't exist
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    # Add to cart
    cart = request.session['cart']
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
    else:
        cart[str(product_id)] = {'quantity': quantity}
    
    request.session.modified = True
    messages.success(request, 'Product added to cart!')
    
    return redirect('cart')


def remove_from_cart(request, product_id):
    if 'cart' in request.session and str(product_id) in request.session['cart']:
        del request.session['cart'][str(product_id)]
        request.session.modified = True
    
    return redirect('cart')


def update_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        return remove_from_cart(request, product_id)
    
    if quantity > product.stock:
        messages.error(request, f'Maximum available quantity is {product.stock}')
        quantity = product.stock
    
    if 'cart' in request.session and str(product_id) in request.session['cart']:
        request.session['cart'][str(product_id)]['quantity'] = quantity
        request.session.modified = True
    
    return redirect('cart')


def checkout(request):
    # Check if cart is empty
    if 'cart' not in request.session or not request.session['cart']:
        messages.error(request, 'Your cart is empty!')
        return redirect('cart')
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        address = request.POST.get('address')
        
        # Validate form data
        if not all([customer_name, customer_email, address]):
            messages.error(request, 'Please fill in all required fields')
            return redirect('checkout')
        
        # Create orders for each product in cart
        for item_id, item_data in request.session['cart'].items():
            product = get_object_or_404(Product, id=int(item_id))
            quantity = int(item_data['quantity'])
            
            if quantity <= product.stock:
                # Create order
                Order.objects.create(
                    product=product,
                    quantity=quantity,
                    customer_name=customer_name,
                    customer_email=customer_email,
                    address=address
                )
                
                # Update product stock
                product.stock -= quantity
                product.save()
            else:
                messages.error(request, f'{product.name} is out of stock!')
                return redirect('checkout')
        
        # Clear cart
        del request.session['cart']
        request.session.modified = True
        
        messages.success(request, 'Your order has been placed successfully!')
        return redirect('order_success')
    
    # Calculate cart totals for the template
    cart_items = []
    total = 0
    
    if 'cart' in request.session:
        for item_id, item_data in request.session['cart'].items():
            product = get_object_or_404(Product, id=int(item_id))
            quantity = int(item_data['quantity'])
            subtotal = product.price * quantity
            total += subtotal
            
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'products/checkout.html', context)


def order_success(request):
    return render(request, 'products/order_success.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
