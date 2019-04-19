from django.contrib import admin
from .models import Country, Client, Currency, Order, Category, Product, Cart, Shipment, PaymentTerm, Payment
# from django.contrib.admin import AdminSite

# class MyAdminSite(AdminSite):
#     site_header = 'WIKKON'
#     site_title ="WIKKON"

# admin_site = MyAdminSite(name='WIKKON')

# Register your models here.

# class MyModelAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(MyModelAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(author=request.user)

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
    list_display = ['date', 'sales', 'sc_no', 'get_client_country', 'client','amount','currency', 'status']
    list_filter = ('date','status','sales__name')
    list_per_page = 20
    search_fields = ['sc_no', 'client__name']

    def get_client_country(self, object):
        return object.client.country.name
    # get_client_name.admin_order_field = 'client'
    get_client_country.short_description = 'Country'

    # fieldsets = (
    #     (None,('fields':())),
    # )
    fields = (('date', 'client'),('pi_no','po_no', ),('sc_no', 'amount'), ('currency','status'),'remarks')
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
    list_display = ['date', 'get_sales','get_sc_no', 'get_client','amount', 'currency', 'term']
    list_filter = ('date',)
    list_per_page = 20
    search_fields = ['order__sc_no']

    def get_sc_no(self, object):
        return object.order.sc_no
    # get_client_name.admin_order_field = 'client'
    get_sc_no.short_description = 'Contract_No'

    def get_client(self, object):
        return object.order.client.name
    # get_client_name.admin_order_field = 'client'
    get_client.short_description = 'Client'

    def get_sales(self, object):
        return object.order.sales.name
    get_sales.admin_order_field = 'sales'
    get_sales.short_description = 'Client'    

admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentTerm)

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['bl_date', 'get_sales','get_sc_no', 'carrier','tracking_no', 'bill_no', 'term']
    list_filter = ('bl_date',)
    list_per_page = 20
    search_fields = ['order__sc_no']

    def get_sc_no(self, object):
        return object.order.sc_no
    # get_client_name.admin_order_field = 'client'
    get_sc_no.short_description = 'Contract_No'

    def get_sales(self, object):
        return object.order.sales.name
    get_sales.admin_order_field = 'sales'
    get_sales.short_description = 'Client'     

admin.site.register(Shipment, ShipmentAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['get_order_date', 'serial_no','get_sc_no']
    list_filter = ('bl_date',)
    list_per_page = 20
    search_fields = ['order__sc_no', 'serial_no']

    def get_order_date(self, object):
        return object.order.date
    # get_client_name.admin_order_field = 'client'
    get_order_date.short_description = 'Order Date'

    def get_sc_no(self, object):
        return object.order.sc_no
    # get_client_name.admin_order_field = 'client'
    get_sc_no.short_description = 'Contract_No'    

admin.site.register(Cart, CartAdmin)

admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Country)
