import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laka.settings")
django.setup()

from product.models import BasicInformation, Manufacturer, Product, Color, ColorProduct

CSV_PATH_PRODUCTS = '/Users/teddyjung/Desktop/laka_prod_color.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        product_name=row[0]
        prod_id  = Product.objects.get(name=product_name).id
        #print(row[1])
        for row1 in row[1].split(', '):
            color_name = row1
            color_id = Color.objects.get(name=color_name).id
            #print(color_name)
            #print(color_id)
            ColorProduct.objects.create(
                product_id=prod_id,
                color_id=color_id
        )
