from django.shortcuts import render,HttpResponse

from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available = True)
    context = {
        'product': products,
    }
    print(products)
    return render(request, 'home.html',context)