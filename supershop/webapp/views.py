from django.shortcuts import render,redirect
from superapp.models import categorydb,productdb
from webapp.models import Registerdb

# Create your views here.
def home_pg(req):
    data=categorydb.objects.all()
    return render(req,"Home.html",{'data':data})
def about_us(req):
    return render(req,"About.html")
def contact_us(req):
    return render(req,"Contact.html")
def cat_pg(req):
    data=categorydb.objects.all()
    return render(req,"Category.html",{'data':data})
def prod_pg(req,cat_name):
    prod=productdb.objects.filter(Category=cat_name)
    return render(req,"product.html",{'prod':prod})
def cart_pg(req):
    return render(req,"cart.html")
def singleproductpage(request,dataid):
    prosingle=productdb.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'prosingle':prosingle})
def registrationpage(request):
    return render(request,"Register.html")

def user_register(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        em=request.POST.get('email')
        mob=request.POST.get('mobnum')
        pwd=request.POST.get('passwd')
        im =request.FILES['img']
        obj=Registerdb(Username=un,Email=em,Mobile=mob,Password=pwd,Image=im)
        obj.save()
        return redirect(registrationpage)