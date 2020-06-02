
import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laka.settings")
django.setup()

from product.models import Color

CSV_PATH_PRODUCTS = '/Users/teddyjung/Desktop/color_url.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        #print(row)
        Color.objects.create(
            name=row[0],
            image_url=row[1],
         )
