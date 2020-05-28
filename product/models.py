from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name                    = models.CharField(max_length=50)
    price_krw               = models.DecimalField(max_digits=10, decimal_places=2)
    description             = models.CharField(max_length=100)
#    shpping_information     = models.ForeignKey('ShippingInformation', on_delete = models.SET_NULL, null=True)
    basic_information       = models.ForeignKey('BasicInformation', on_delete = models.SET_NULL, null=True)
    launch_date             = models.DateField()
    caution                 = models.CharField(max_length=3000)
    volume_g                = models.DecimalField(max_digits=10, decimal_places=2)
    mfds                    = models.CharField(max_length=300)
    how_to_use              = models.CharField(max_length=500)
    is_limited              = models.BooleanField(default=False)
    inner_image_url         = models.URLField(max_length=2000)
    outer_front_image_url   = models.URLField(max_length=2000)
    outer_back_image_url    = models.URLField(max_length=2000)
    category                = models.ManyToManyField(Category,through='CategoryProduct', related_name='categories')
    color                   = models.ManyToManyField('Color', through='ColorProduct', related_name='colors')
    manufacturer            = models.ManyToManyField('Manufacturer', through='ManufacturerProduct',related_name='manufacturers')

    class Meta:
        db_table = 'products'

class CategoryProduct(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product     = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'categories_products'

class Color(models.Model):
    name        = models.CharField(max_length=20)
    image_url   = models.URLField(max_length=2000)

    class Meta:
        db_table = 'colors'

class ColorProduct(models.Model):
    color   = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'colors_products'

class BasicInformation(models.Model):
    return_policy       = models.CharField(max_length=2000)
    customer_service    = models.CharField(max_length=2000)
    expiration          = models.CharField(max_length=100)
    quality_assurance   = models.CharField(max_length=2000)
    main_spec           = models.CharField(max_length=100)

    class Meta:
        db_table = 'basic_information'

class Manufacturer(models.Model):
    name            = models.CharField(max_length=100)
    country_name    = models.CharField(max_length=50)

    class Meta:
        db_table = 'manufacturer'

class ManufacturerProduct(models.Model):
    manufacturer    = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    product         = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'manufacturers_products'
