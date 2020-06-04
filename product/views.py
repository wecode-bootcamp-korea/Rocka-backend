import json
import jwt

from django.http    import JsonResponse
from django.shortcuts import render
from django.views import View

from .models    import Product,Category,Color

class ProductView(View):
    def get(self, request):
        query       = request.GET.get('category',None)
        filtering_data   = {}
        if query:
            filtering_data['category__name']= query
        all_prod        = Product.objects.all().filter(**filtering_data).prefetch_related('categoryproduct_set','colorproduct_set')

        products=[{
        'id'                    : prod.id,
        'name'                  : prod.name,
        'price_krw'             : prod.price_krw,
        'description'           : prod.description,
        'category'              :
        [category.category.name for category in prod.categoryproduct_set.all()],
        'color'                 : [{
            'name'          : element.color.name,
            'stock_quantity': element.stock_quantity,
            'image_url'     : element.color.image_url
        } for element in prod.colorproduct_set.all()],
        'outer_front_image_url' : prod.outer_front_image_url,
        'outer_back_image_url'  : prod.outer_back_image_url,
        'launchdate'            : prod.launch_date
        } for prod in all_prod]

        if len(products)>0:
            return JsonResponse({'data':products}, status=200)
        else:
            return JsonResponse({'message':'BAD_REQUEST'}, status=400)

class CategoryView(View):
    def get(self, request):
        all_category    = Category.objects.all().prefetch_related('product_set')
        category_info = [{
            'category_id'   : category.id,
            'name'          : category.name,
            'count'         : len(category.product_set.all())
            } for category in all_category]
        return JsonResponse({'data':category_info}, status=200)

class DetailView(View):
    def get(self, request,product_id):
        try:
            product         = Product.objects.select_related('basic_information').prefetch_related(
                'color','manufacturer'
            ).get(id=product_id)
            basic_info      = product.basic_information
            color_info      = product.color.all()
            manufac_info    = product.manufacturer.all()
            order_quantity  = 1
            product_info    = {
                'id'                : product_id,
                'name'              : product.name,
                'description'       : product.description,
                'price_krw'         : product.price_krw,
                'return_policy'     : basic_info.return_policy,
                'customer_service'  : basic_info.customer_service,
                'expiration'        : basic_info.expiration,
                'quality_assurance' : basic_info.quality_assurance,
                'main_spec'         : basic_info.main_spec,
                'caution'           : product.caution,
                'volume_g'          : product.volume_g,
                'mfds'              : product.mfds,
                'how_to_use'        : product.how_to_use,
                'inner_image_url'   : product.inner_image_url,
                'manufacturer'      : [{
                    'name'          : manufac.name,
                    'country_name'  : manufac.country_name
                } for manufac in manufac_info],
                'color'                 : [{
                    'name'              : color.name,
                    'order_quantity'    : order_quantity,
                    'image_url'         : color.image_url
                } for color in color_info]
            }
            return JsonResponse({'data':product_info}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({'message':'BAD_REQUEST'}, status=400)
