from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from store.models import Product, Cart, Wishlist
from django.contrib.auth.decorators import login_required
from store.models import Order, OrderItem, Profile
from django.contrib.auth.models import User


def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, "orders/index.html", context)
    

def vieworder(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'orderitems':orderitems}
    return render(request, "orders/view.html", context)
    











































































