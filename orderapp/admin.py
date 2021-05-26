from django.contrib import admin
from orderapp.models import ShopCart, Order, OrderProduct
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display=['product','user','quantity','price','amount','price']
list_filter=['user']


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0



class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'phone', 'total', 'status', 'transaction_id']
    list_filter = ['status','code']
    search_fields = ('status', 'code', 'first_name','last_name', 'phone' )
    readonly_fields = ('user', 'first_name', 'last_name',
                       'phone', 'address', 'city', 'country', 'total', 'ip', 'transaction_id', 'image_tag')
    can_delete = False
    inlines = [OrderProductline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user','created_at']
    search_fields = ('user', 'price', 'product','quantity', 'created_at' )



admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)