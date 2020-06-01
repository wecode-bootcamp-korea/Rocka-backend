import json
import jwt

from django.http    import JsonResponse
from django.shortcuts import render
from django.views import View

from .models    import Product

class ProductView(View):
    def get(self, request):
        all_prod = Product.objects.all()
        products= []
        for prod in all_prod:
            category            = [category.category.name for category in prod.categoryproduct_set.all()]
            color_name_stock    = [{
                'name'          : element.color.name,
                'stock_quantity': element.stock_quantity,
                'image_url'     : element.color.image_url
            } for element in prod.colorproduct_set.all()]
            products.append({
                'id'                    : prod.id,
                'name'                  : prod.name,
                'price_krw'             : prod.price_krw,
                'description'           : prod.description,
                'category'              : category,
                'color'                 : color_name_stock,
                'outer_front_image_url' : prod.outer_front_image_url,
                'outer_back_image_url'  : prod.outer_back_image_url,
                'launchdate'            : prod.launch_date
            })
        return JsonResponse({'data':products}, status=200)
