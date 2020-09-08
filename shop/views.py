from django.shortcuts import render

from django.http import HttpResponse
from . models import Post,Contact

def index(request):
    products=Post.objects.all();
    # print(prod)
    n=len(products);
    nslide=n//4+(n%4!=0);
    param={'no_of_slides':nslide, 'range':range(1,nslide),'product':products};
    return render(request,'shop/index.html',param);

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    name=request.POST.get('name','');
    email=request.POST.get('email','');
    phone=request.POST.get('phone','');
    desc=request.POST.get('desc','');
    x=Contact(name=name,email=email,phone=phone,desc=desc);
    x.save();
    return render(request,'shop/contact.html')

def productview(request, prodid):
    #Fetch the product using the id
    product=Post.objects.get(id=prodid)
    # print(product);
    return render(request,'shop/prodview.html',{'product':product});

def checkout(request):
    return render(request,'shop/checkout.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')
# Create your views here.
