from django.contrib import admin
from .models import Country, Client, Currency, Order, Category, Product, Cart, Shipment, PaymentTerm, Payment
# from django.contrib.admin import AdminSite

# class MyAdminSite(AdminSite):
#     site_header = 'WIKKON'
#     site_title ="WIKKON"

# admin_site = MyAdminSite(name='WIKKON')

# Register your models here.

class CartInline(admin.TabularInline):
    model = Cart
    extra = 1

class ShipmentInline(admin.TabularInline):
    model = Shipment
    extra = 1

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['date', 'sc_no', 'get_client_country', 'client','amount','currency']
    list_filter = ('date',)
    list_per_page = 20
    search_fields = ['sc_no', 'client__name']

    def get_client_country(self, object):
        return object.client.country.name
    # get_client_name.admin_order_field = 'client'
    get_client_country.short_description = 'Country'

    # fieldsets = (
    #     (None,('fields':())),
    # )
    fields = (('date', 'client'),('pi_no','po_no', ),('sc_no', 'amount'), 'currency')
    inlines =[CartInline, ShipmentInline, PaymentInline]
    raw_id_fields = ('client',)

admin.site.register(Order, OrderAdmin)

class ClinetAdmin(admin.ModelAdmin):
    list_display = ['name','tag','country','contact','email','phone']
    search_fields = ['name','country']
    list_per_page = 20

admin.site.register(Client, ClinetAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['model','category']

admin.site.register(Product, ProductAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['date', 'get_sc_no', 'amount', 'currency', 'term']
    list_filter = ('date',)
    list_per_page = 20
    search_fields = ['order__sc_no']

    def get_sc_no(self, object):
        return object.order.sc_no
    # get_client_name.admin_order_field = 'client'
    get_sc_no.short_description = 'Contract_No'

admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentTerm)
admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Country)
