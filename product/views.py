import json
import jwt

from django.http    import JsonResponse
from django.shortcuts import render
from django.views import View

from .models    import Product,Category

class ProductView(View):
    def get(self, request):
        all_prod = Product.objects.all()
        products=[{
            'id'                    : prod.id,
            'name'                  : prod.name,
            'price_krw'             : prod.price_krw,
            'description'           : prod.description,
            'category'              : [category.category.name for category in prod.categoryproduct_set.all()],
            'color'                 : [{
                'name'          : element.color.name,
                'stock_quantity': element.stock_quantity,
                'image_url'     : element.color.image_url
            } for element in prod.colorproduct_set.all()],
            'outer_front_image_url' : prod.outer_front_image_url,
            'outer_back_image_url'  : prod.outer_back_image_url,
            'launchdate'            : prod.launch_date
        } for prod in all_prod]
        return JsonResponse({'data':products}, status=200)


class CategoryView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        products = category.categories.all()
        try:
            category_info = {'name' : category.name}
            products_info = [{
                'id'                    : prod.id,
                'name'                  : prod.name,
                'price_krw'             : prod.price_krw,
                'description'           : prod.description,
                'category'              : [category.category.name
                                           for category in prod.categoryproduct_set.all()],
                'color'                 : [{
                    'name'          : element.color.name,
                    'stock_quantity': element.stock_quantity,
                    'image_url'     : element.color.image_url
                } for element in prod.colorproduct_set.all()],
                'outer_front_image_url' : prod.outer_front_image_url,
                'outer_back_image_url'  : prod.outer_back_image_url,
            } for prod in products]

            return JsonResponse({'category':category_info,'product':products_info}, status=200)
        except Category.DoesNotExist:
            return JsonResponse({'message':'INVALID_CATEGORY'}, status=400)
