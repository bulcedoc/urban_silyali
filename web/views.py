from django.shortcuts import render,redirect
from django.http import HttpResponse
from ad.models import Category,Product,Product_images
import requests,random
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def web_home(request):
    p = Product.objects.all().order_by('product_sale')[:5]
    c = Category.objects.all().order_by('category_sale')[:5]
    return render(request,'main.html',context = {'c':c,'p':p})

def products(request,pk):

    p = Product.objects.filter(product_category=pk)
    cat = p[0].product_category
    return render(request,'products.html',context={'p':p,'cat':cat})

def view_product(request,pk):
    p = Product.objects.get(product_id=pk) 
    img = Product_images.objects.filter(product=pk)
    if len(img)>1 :
     return render(request,'view.html',context={'p':p,'img':img[1:],'pa':img[0]})
    return render(request,'view_no.html',context={'p':p,'img':img})
def shop(request):
    c = Category.objects.all()
    return render(request,'cat.html',context={'c':c})

def signup(request):
    if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      password = request.POST.get('password')
      address = request.POST.get('add')
      user = authenticate(request=None, phone =phone, password = password)
      if user is not None:
         login(request,user)
         messages.error(request,'Logged in as '+user.name)
         if(request.session['url']):
          url = request.session['url']
         response = redirect(url)
         return response
      else:
         messages.error(request,'Wrong credentials')
         return render(request, 'pos/pos_login.html')
    else:
       return render(request,'login.html')    





def send_otp(num):
 otp= random.randrange(100000,999999)   
 url = "https://www.fast2sms.com/dev/bulkV2"
 payload = "variables_values="+otp+"&route=otp&numbers="+num
 headers = {
    'authorization': "voBV6U9L8xZmINfnc4tgebluh1Or3YpHF7yJG5aEis2TWAPj0RtqKrmuLXdCoHpQV4xZnPaj2Rcgz087",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
 response = requests.request("POST", url, data=payload, headers=headers)
 print(response.text)
 return(response.text)