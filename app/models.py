

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
State_Choice = (
    ('bhalwal','bhalwal'),
    ('sargodha','sargodha'),
    ('lahore','lahore'),
    ('karachi','karachi'),
)
class Customer(models.Model):
      Customer = models.ForeignKey(User,on_delete=models.CASCADE)
      name = models.CharField(max_length=20)
      locality = models.CharField(max_length=30)
      city = models.CharField(max_length=20)
      zipcode = models.IntegerField()
      state = models.CharField(choices=State_Choice,max_length=30)

      def __str__(self):
        return str(self.id)
category_choice = (
    ('tp','topwear'),
    ('bt','botomwear'),
    ('mobil','mobiles'),
    ('lp','laptop'),
)

class product(models.Model):
    title = models.CharField(max_length=40)
    price = models.FloatField(max_length=30)
    discounted_price = models.FloatField(max_length=20)
    descrption = models.TextField()
    brand = models.CharField(max_length=20,default='redmi')
    categori = models.CharField(choices=category_choice,max_length=10)
    product_img = models.ImageField(upload_to='images/')

    def __str__(self):
      return str(self.id)


order_status =(
    ('accepted','accepted'),
    ('on the way','on the way'),
    ('Dileverd','Dileverd'),
    ('cancel','cancel'),
)

class order_placed(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date =models.DateTimeField(auto_now_add=True)

    status = models.CharField(choices=order_status,max_length=20,default='pending') 

    def __str__(self):
      return str(self.id)

class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
