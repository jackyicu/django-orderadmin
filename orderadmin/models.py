from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    country = models.ForeignKey(Country, on_delete = None)
    contact = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    fax = models.CharField(max_length=15, blank=True)
    tag = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % (self.name)

class Currency(models.Model):
    name = models.CharField(max_length=3)
    
    def __str__(self):
        return self.name

class Sales(models.Model):
    name = models.CharField(max_length=8, default='admin')

    def __str__(self):
        return self.name    

class Order(models.Model):
    date = models.DateField(verbose_name='Order Date')
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE, blank=True)
    pi_no = models.CharField(max_length=15)
    po_no = models.CharField(max_length=15, blank=True)
    sc_no = models.CharField(max_length=15, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    currency = models.ForeignKey(Currency,on_delete=None, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True)
    remarks = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.sc_no

class Category(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.model

class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    erp_code = models.CharField(max_length=9, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=8, blank=True)
    location = models.CharField(max_length=30, blank=True)
    installation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.serial_no    

class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)   
    bl_date = models.DateField(blank=True, null=True)
    carrier = models.CharField(max_length=10, blank=True)
    tracking_no = models.CharField(max_length=20, blank=True)
    bill_no = models.CharField(max_length=10, blank=True)
    fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.bill_no

class PaymentTerm(models.Model):
    type = models.CharField(max_length=5)

    def __str__(self):
        return self.type

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency,on_delete=None, blank=True, null=True)
    term = models.ForeignKey(PaymentTerm, on_delete=None, blank=True, null=True)

    # def __str__(self):
    #     return self.amount





    

