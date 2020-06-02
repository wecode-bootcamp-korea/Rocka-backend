
import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laka.settings")
django.setup()

from product.models import Product

CSV_PATH_PRODUCTS = '/Users/teddyjung/Desktop/laka_all_prod_info.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        #print(row)
        Product.objects.create(
            name=row[0],
            caution=row[1],
            volume_g=row[2].split(' ')[0],
            price_krw=row[8].split(' ')[1],
            description=row[7],
            launch_date=row[12],
            mfds=row[5],
            how_to_use=row[4],
            inner_image_url=row[11],
            outer_front_image_url=row[9],
            outer_back_image_url=row[10],
         )
