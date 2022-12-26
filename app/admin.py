
from django.contrib import admin
from .models import(
    Customer,
    order_placed,
    product,
    cart,
)
# Register your models here.
@admin.register(Customer)
class CustomerModeladmin(admin.ModelAdmin):
    list_display = ['id','name','locality','city','zipcode','state'
    ]

@admin.register(product)
class productModeladmin(admin.ModelAdmin):
    list_display = ['id','title','price','descrption','categori','product_img','brand'
    ]

@admin.register(order_placed)
class order_placedModeladmin(admin.ModelAdmin):
    list_display = ['id','user','user','order_date','status','product'
    ]

@admin.register(cart)
class cartModeladmin(admin.ModelAdmin):
    list_display = ['id','product','user','quantity'
    ]