import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laka.settings")
django.setup()

from product.models import BasicInformation, Manufacturer, Product

CSV_PATH_PRODUCTS = '/Users/youngbinha/Desktop/laka_all_prod_info.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
    #    print(row[8].split)
        prod_name = row[0]
        prod = Product.objects.get(name=prod_name)
        prod.description = row[7]
        prod.save()
