from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from shop.models import (CartItem, Item, Cart)
from django.urls import reverse

# CRUD
# CREATE
# READ
# UPDATE
# DELETE

def index(request):
  cart = Cart.objects.first()
  cart = [{"item": cart_item.item, "count": cart_item.count} for cart_item in cart.items.all()]
  return render(request, "shop.html", { "cart_size": len(cart), "cart": cart, "items": Item.objects.all() })


def add_to_cart(request, item_uuid):
  item = get_object_or_404(Item, pk=item_uuid)
  
  if Cart.objects.count() == 0:
    Cart.objects.create()
  
  cart = Cart.objects.first()

  try:
    cart_item = CartItem.objects.get(item=item)
    cart_item.count += 1
    cart_item.save()
  except CartItem.DoesNotExist:
    cart_item = CartItem.objects.create(item=item, count=1)
  
  cart.items.add(cart_item)
  cart.save()
  
  return HttpResponseRedirect(reverse("shop:index"))


def reduce_from_cart(request, item_uuid):
  item = get_object_or_404(Item, pk=item_uuid)
  
  if Cart.objects.count() == 0:
    Cart.objects.create()
    
  cart = Cart.objects.first()
  
  try:
    cart_item = CartItem.objects.get(item=item)
    if cart_item.count == 1:
      cart.items.remove(cart_item)
      cart_item.delete()
    else:
      cart_item.count -= 1
      cart_item.save()
  except CartItem.DoesNotExist:
    return Http404("Something went wrong!")
  
  return HttpResponseRedirect(reverse("shop:index"))