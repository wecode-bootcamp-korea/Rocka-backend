from django.db import models

class Member(models.Model):
    nickname        = models.CharField(max_length=50)
    fullname        = models.CharField(max_length=50)
    email           = models.CharField(max_length=300, default="")
    phone_number    = models.CharField(max_length=50)
    address         = models.CharField(max_length=500, null=True)
    password        = models.CharField(max_length=300, default="")
    gender          = models.ForeignKey('Gender', on_delete = models.SET_NULL, null=True)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'members'

class Gender(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'genders'

class ShippingAddress(models.Model):
    destination  = models.CharField(max_length=100)
    receiver     = models.CharField(max_length=50)
    address      = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=50)
    member       = models.ForeignKey(Member, on_delete = models.SET_NULL, null=True)
    is_default   = models.BooleanField(default=False)

    class Meta:
        db_table = 'shipping_addresses'
