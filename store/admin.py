from django.contrib import admin
from .models import User, Products, CartItems

admin.site.register(User)
admin.site.register(Products)
admin.site.register(CartItems)
