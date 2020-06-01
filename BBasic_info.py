
import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laka.settings")
django.setup()

from product.models import BasicInformation, Manufacturer, Product

CSV_PATH_PRODUCTS = '/Users/youngbinha/Desktop/laka_basic.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        print(row)
        BasicInformation.objects.create(
            main_spec=row[3],
            return_policy=row[7],
            customer_service=row[6],
            expiration=row[8],
            quality_assurance=row[11]
         )
