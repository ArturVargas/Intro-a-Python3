from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(req):
  list_products = Product.objects.all()
  return render(req, 'index.html', {'products': list_products})

def new(req):
  return HttpResponse('New Products')
