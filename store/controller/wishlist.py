from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from store.models import Product, Cart, Wishlist
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request, 'store/wishlist.html', context) 

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.filter(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id = prod_id)):
                    return JsonResponse({"status":"Product already in wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({"status":"Product added to wishlist"})
            else:
                    return JsonResponse({"status":"No such product found"})
        else:
            return JsonResponse({"status":"Login to continue"})
    return redirect('/')


def  detetewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id')) 
            if(Wishlist.objects .filter(user=request.user, product_id=prod_id)):
                
                wishlistitem = Wishlist.objects.get(product_id=prod_id, user=request.user)
                wishlistitem.delete() 
                return JsonResponse({"status":"Product removed from wishlist"})
            
            else:
                return JsonResponse({"status":"Product not found in wishlist"})
        return JsonResponse({"status":"Login to continue"})
    
    return redirect('/')





























