from django.contrib import admin
from shop.models import (CartItem, Item, Cart)

class ItemAdmin(admin.ModelAdmin):
  list_display = ("pk", "name", "price", "pub_date")

admin.site.register(Item, ItemAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)