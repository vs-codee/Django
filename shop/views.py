from django.shortcuts import render

from django.http import HttpResponse
from . models import Post,Contact,Orders

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
    product=Post.objects.get(id=prodid);

    # print(product);
    return render(request,'shop/prodview.html',{'product':product});

def checkout(request):
    ok=False;
    if request.method=="POST":
        json=request.POST.get('json','');
        name=request.POST.get('name','');
        email=request.POST.get('email','');
        address=request.POST.get('address1','') + ' '+request.POST.get('address2','');
        city=request.POST.get('city','');
        state=request.POST.get('state','');
        zipcode=request.POST.get('zipcode','');
        phone=request.POST.get('phone','');
        order=Orders(json=json,name=name,email=email,address=address,state=state,city=city,zipcode=zipcode,phone=phone);
        order.save();
        ok=True;
    return render(request,'shop/checkout.html',{'ok':ok})

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')
# Create your views here.
