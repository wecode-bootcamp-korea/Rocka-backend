import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laka.settings")
django.setup()

from store.models import Store

CSV_PATH_PRODUCTS = '/Users/teddyjung/Desktop/output.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
    #    print(row[8].split)
        Store.objects.create(
            name=row[0],
            branch=row[1],
            phone_number=row[2],
            address=row[3],
            store_time=row[4],
            map_url=row[5],
       )
