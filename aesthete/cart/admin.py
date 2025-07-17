from django.contrib import admin

from cart.models import Usercart, Cartitems

admin.site.register(Usercart)
admin.site.register(Cartitems)

