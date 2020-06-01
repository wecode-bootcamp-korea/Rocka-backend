import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laka.settings")
django.setup()

from product.models import Color

CSV_PATH_PRODUCTS = './product_color.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    for row in data_reader:
        print(row)
