from django.shortcuts import render

from shopcart.models import Product
from django.db.models import Q



def searchResult(request):
    query=None
    products=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        context={'query':query,'products':products}
    return render(request,'search.html',context)

