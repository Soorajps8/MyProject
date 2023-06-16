from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from superapp.models import categorydb,productdb
from django.contrib import messages


# Create your views here.
def index_page(req):
    return render(req,"Indexpage.html")
def add_category(req):
    return render(req,"AddCategory.html")
def cat_add(req):
    if req.method=="POST":
        na=req.POST.get('cname')
        im=req.FILES['img']
        descp=req.POST.get('descript')
        obj=categorydb(Category_Name=na,Category_Image=im,Description=descp)
        obj.save()
        messages.success(req,"Category Saved Successfully")
        return redirect(add_category)

def display_category(req):
    data=categorydb.objects.all()
    return render(req,"Displaycategory.html",{'data':data})
def delete_cate(req,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_category)
def editcateg(req,catid):
    category=categorydb.objects.get(id=catid)
    return render(req,"Editcategory.html",{'category':category})
def update_cate(req,catid):
    if req.method=="POST":
        na = req.POST.get('cname')
        descp = req.POST.get('descript')
    try:
        im=req.FILES['img']
        fs=FileSystemStorage()
        file=fs.save(im.name,im)
    except MultiValueDictKeyError:
        file=categorydb.objects.get(id=catid).Category_Image
    categorydb.objects.filter(id=catid).update(Category_Name=na,Category_Image=file,Description=descp)
    return redirect(display_category)


def productadd(req):
    data=categorydb.objects.all()
    return render(req,"Addproduct.html",{'data':data})

def addproduct(req):
    if req.method=="POST":
        cn=req.POST.get('caname')
        pn=req.POST.get('pname')
        pr=req.POST.get('pprice')
        ds=req.POST.get('desc')
        pim=req.FILES['file']
        obj1=productdb(Category=cn, Product_Name=pn, Price=pr,Description=ds,Image=pim)
        obj1.save()
        return redirect(productadd)

def displayproduct(req):
    product=productdb.objects.all()
    return render(req,"Displayproduct.html",{'product':product})
def editproduct(req,productid):
    category=categorydb.objects.all()
    product=productdb.objects.get(id=productid)
    return render(req,"Editproduct.html",{'product':product,'category':category})
def deleteproduct(request,productid):
    data=productdb.objects.filter(id=productid)
    data.delete()
    return redirect(displayproduct)

def updateproduct(req,productid):
    if req.method=="POST":
        cn=req.POST.get('caname')
        pn=req.POST.get('pname')
        pr=req.POST.get('pprice')
        ds=req.POST.get('desc')
    try:
        pim=req.FILES['pimg']
        fs=FileSystemStorage()
        file=fs.save(pim.name,pim)
    except MultiValueDictKeyError:
        file=productdb.objects.get(id=productid).Image
    productdb.objects.filter(id=productid).update(Category=cn, Product_Name=pn, Price=pr,Description=ds,Image=file)
    return redirect(displayproduct)

def ad_login(req):
    return render(req,"login_admin.html")
def admin_log(req):
    if req.method=="POST":
        uname=req.POST.get("uname")
        pwd=req.POST.get("pwd")
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(req,user)
                req.session['username']=uname
                req.session['password']=pwd
                return redirect(index_page)
            else:
                return redirect(ad_login)
        else:
            return redirect(ad_login)

def log_out(req):
    del req.session['username']
    del req.session['password']
    return redirect(ad_login)




