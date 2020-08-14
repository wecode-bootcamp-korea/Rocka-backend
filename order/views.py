import json
import jwt, bcrypt

from django.views     import View
from django.http      import HttpResponse, JsonResponse
from decimal          import Decimal
from datetime import datetime

from member.models import Member, ShippingAddress
from member.views import LoginConfirm
from laka.settings import SECRET_KEY

from order.models import (
    Order,
    PaymentMethod,
    OrderStatus,
    ShippingInformation,
    OrderDetail
)
from product.models import (
    Category,
    Product,
    Color,
)
class CartView(View):
    @LoginConfirm
    def post(self, request):
        try:
            data                    = json.loads(request.body)
            nickname                = request.user
            now                     = datetime.now()
            ordernumber             = f"{nickname.id}{now.year}{now.month}{now.day}{now.hour}{now.minute}"
            if Order.objects.filter(member_id=nickname.id, order_status=1).exists():
                order = Order.objects.filter(order_status=1).last()
            else:
                order = Order.objects.create(
                    order_num       = ordernumber,
                    order_status    = OrderStatus.objects.get(id=1),
                    member          = nickname
                )
            for elem in data:
                prod = OrderDetail.objects.filter(order_id=order.id)
                ordered_color_name      = elem['name']
                ordered_quantity        = int(elem['order_quantity'])
                if not Color.objects.filter(name=ordered_color_name).exists():
                    return JsonResponse({"message":"CHECK_COLOR_NAME"}, status=404)
                if prod.exists():
                    if prod.filter(color__name=elem['name']):
                        prod.filter(color__name=elem['name']).update(quantity=ordered_quantity)
                    else:
                        OrderDetail.objects.create(
                                product_id      = Product.objects.get(id=elem['id']).id,
                                quantity        = ordered_quantity,
                                color_id        = Color.objects.get(name=ordered_color_name).id,
                                order_id        = order.id
                            )
            return HttpResponse(status=200)
        except KeyError:
            return HttpResponse(status=400)
        except Product.DoesNotExist:
            return JsonResponse({"message":"INVAILD_VALUE"}, status=404)

    @LoginConfirm
    def get(self, request):
        try:
            user = request.user
            cart_items = Order.objects.get(member=user, order_status=1).orderdetail_set.all().select_related('product','color')

            mycart=[{
                'name'                  : item.product.name,
                'outer_front_image_url' : item.product.outer_front_image_url,
                'order_quantity'        : item.quantity,
                'price_krw'             : item.product.price_krw,
                'color_name'            : item.color.name
            } for item in cart_items]

            return JsonResponse({'data':mycart}, status=200)

        except:
            return HttpResponse(status=401)
