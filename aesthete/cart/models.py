from django.db import models
import uuid
from store.models import Products

class Usercart(models.Model):
    cart_id = models.UUIDField(default = uuid.uuid4, editable = False, primary_key = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.cart_id)

class Cartitems(models.Model):
    cart = models.ForeignKey(Usercart, on_delete = models.CASCADE, related_name = 'items', null = True, blank = True)
    product = models.ForeignKey(Products, on_delete = models.CASCADE, related_name = 'cartitems', null = True, blank = True)
