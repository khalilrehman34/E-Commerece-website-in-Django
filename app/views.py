
from django.http import JsonResponse, request
from .models import product
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,cart
from .form import userregisterion,profilee
from django.db.models import Q
class products(View):
    def get(self,request):
     topwear = product.objects.filter(categori='tp')
     bottomwear = product.objects.filter(categori='bt')
     mobile=product.objects.filter(categori='mobil')
     return render(request, 'app/home.html',{'topwear':topwear,'bottomwear':bottomwear})

class product_detail(View):
      def get(self,request,pk):
        products = product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'products':products})

def add_to_cart(request):
   user = request.user
   product_id = request.GET.get('prod_id')
   products = product.objects.get(id=product_id)
   cart(user=user,product=products).save()
   return redirect('/cart')

def show_cart(request):
   user = request.user
   products = cart.objects.filter(user=user)
   amount = 0.0
   shipping_amount = 30.0
   total_amount = 0.0
   cart_product = [p for p in cart.objects.all() if p.user == user]
   if cart_product :
      for p in cart_product:
         tempamount = (p.quantity * p.product.price )
         amount += tempamount
         total_amount = amount + shipping_amount 
      return render(request, 'app/addtocart.html',{'products':products,'amount':amount,
       'total_amount':total_amount})
   else:
      return render(request, 'app/emptycart.html')

def plus_cart(request):
   if request.method == 'GET':
      p_id = request.GET['prod_id']
      c = cart.objects.get(Q(product=p_id) & Q(user=request.user))
      c.quantity+=1
      c.save()
      amount = 0.0
      shipping_amount = 30.0
      cart_product = [p for p in cart.objects.all() if p.user == request.user]
      for p in cart_product:
         tempamount = (p.quantity * p.product.price )
         amount += tempamount
         total_amount = amount + shipping_amount 
      data = {
         'quantity':c.quantity,
         'amount':amount,
         'total_amount':total_amount,
       }
      return JsonResponse(data)
def minus_cart(request):
   if request.method == "GET":
      p_id = request.GET['prod_id']
      c =cart.objects.get(Q(product=p_id) & Q(user=request.user))
      c.quantity-=1
      c.save()
      amount=0.0
      shiping_amount = 30.0
      cart_product = [p for p in cart.objects.all() if p.user==request.user]
      for p in cart_product:
         tempamount = (p.quantity * p.product.price )
         amount += tempamount
         total_amount = amount + shiping_amount 
      data = {
         'quantity':c.quantity,
         'amount':amount,
         'total_amount':total_amount,
       }
      return JsonResponse(data)

def remove_cart(request):
    if request.method == "GET":
      p_id = request.GET['prod_id']
      c =cart.objects.get(Q(product=p_id) & Q(user=request.user))
      c.delete()
      amount=0.0
      shiping_amount = 30.0
      cart_product = [p for p in cart.objects.all() if p.user==request.user]
      for p in cart_product:
         tempamount = (p.quantity * p.product.price )
         amount += tempamount
         total_amount = amount + shiping_amount 
      data = {
         'amount':amount,
         'total_amount':total_amount,
       }
      return JsonResponse(data)

      
def buy_now(request):
 return render(request, 'app/buynow.html')

class profileview(View):
   def get(self,request):
      form = profilee()
      return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})
   def post(self,request):
      form = profilee(request.POST)
      if form.is_valid():  
        usr = request.user
        name = form.cleaned_data['name']
        locality = form.cleaned_data['locality']
        city = form.cleaned_data['city']
        zipcode = form.cleaned_data['zipcode']
        state = form.cleaned_data['state']
        reg = Customer(Customer=usr,name=name,locality=locality,city=city,zipcode=zipcode,state=state )
        reg.save()
      return render(request, 'app/profile.html')

def address(request,pk):
    gop = Customer.objects.filter(Customer=pk)
    return render(request, 'app/address.html',{'gop':gop,'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')



def mobile(request,data=None):
    if data == None:
       mobile = product.objects.filter(categori='mobil')
    elif data == 'redmi' or data == 'samsung' :
       mobile = product.objects.filter(categori='mobil').filter(brand=data)
    elif data == 'below':
       mobile = product.objects.filter(categori='mobil').filter(price__lt=10000)
    return render(request, 'app/mobile.html',{'mobile':mobile})

def login(request):
 return render(request, 'app/login.html')



class customerregistration(View):
   def get(self,request):
      form = userregisterion()
      return render(request, 'app/customerregistration.html',{'form':form})

   def post(self,request):
      form = userregisterion(request.POST)
      if form.is_valid():
       form.save()
      return render(request, 'app/customerregistration.html',{'form':form})



def checkout(request):

 return render(request, 'app/checkout.html')
