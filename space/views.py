from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User # May not be in use
from django.http  import HttpResponse,Http404,HttpResponseRedirect,HttpResponseForbidden,JsonResponse
from django.contrib.auth import login, authenticate, get_user_model
import json
from jsil import settings
import urllib
from django.contrib import messages
from .forms import SignupForm,ComposeForm,ImageForm
from .models import *
from django.contrib import messages
from django.conf import settings
import requests
from .decorators import check_recaptcha
from django.http import JsonResponse
from django.views.generic import DetailView, ListView
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin


def homepage(request):
    products = Product.objects.all()
    return render(request, 'homepage.html',locals())
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def search_product(request):
  
    if 'product' in request.GET and request.GET["product"]:
        category = request.GET.get("product")
        searched_products = Product.search_product(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"products": searched_products})

    else:
        message = ".You haven't searched for any category"
        return render(request, 'search.html',{"message":message})


def filter_by_category(request,category_id):
    '''
    Filters the database and displays images according to category_id
    '''
    products = Product.filter_by_category(id = category_id)
    return render(request,'category.html',{"products":products})