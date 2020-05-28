from django.db import models
from member.models import Member, ShippingAddress


class Order(models.Model):
    order_num               = models.CharField(max_length=100)
    payment_method          = models.ForeignKey('PaymentMethod', on_delete = models.SET_NULL, null=True)
    order_status            = models.ForeignKey('OrderStatus', on_delete = models.SET_NULL, null=True)
    shipping_address        = models.ForeignKey(ShippingAddress, on_delete = models.SET_NULL, null=True)
    member                  = models.ForeignKey(Member, on_delete = models.SET_NULL, null=True)
    shipping_information    = models.ForeignKey('ShippingInformation', on_delete =models.SET_NULL, null=True)
    total_amount            = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'orders'

class PaymentMethod(models.Model):
    pay_method              = models.CharField(max_length=50)

    class Meta:
        db_table = 'paymethods'

class OrderStatus(models.Model):
    name                    = models.CharField(max_length=50)

    class Meta:
        db_table = 'names'

class ShippingInformation(models.Model):
    delivery_date_info      = models.CharField(max_length=50)
    shipping_charge         = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'shipping_informations'

class OrderDetail(models.Model):
    quantity                = models.IntegerField(default=0)
    order                   = models.ForeignKey('Order', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'orderdetails'









