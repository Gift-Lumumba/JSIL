from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import datetime as dt
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from multiprocessing import Process
from django.urls import reverse

User = get_user_model()



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Product(models.Model):
    '''
    class that contains product properties,methods and functions
    '''
    post = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=40)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.ForeignKey(Category)

    def __str__(self):
      return self.name

    def save_product(self):
        self.save

    def delete_product(self):
        self.delete

    class Meta:
        ordering = ['posted_on']

    @classmethod
    def get_all_products(cls):
        products = cls.objects.order_by()
        return products

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)


    @classmethod
    def get_product_by_id(cls, id):
        product = Product.objects.filter(user_id=id).all()
        return product

    @classmethod
    def search_product(cls, category):
        products = cls.objects.filter(category__name__icontains=category)
        return products

    @classmethod
    def filter_by_category(cls, id):
        products = cls.objects.filter(category_id=id)
        return products

    @property
    def count_likes(self):
        likes = self.likes.count()
        return likes


    @property
    def count_comments(self):
        comments = self.comments.count()
        return comments

