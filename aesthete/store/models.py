from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200, primary_key = True)
    image_icon = models.TextField()

    def __str__(self):
        return self.name

class Products(models.Model):
    title = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    product_images = models.TextField()
    hashtags = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    


