import json
import jwt, bcrypt

from django.views     import View
from django.http      import HttpResponse, JsonResponse
from decimal          import Decimal
from datetime import datetime

from member.models import Member, ShippingAddress
from member.views import LoginConfirm
from product.models import *
from laka.settings import SECRET_KEY
from order.models import Order, PaymentMethod, OrderStatus, ShippingInformation, OrderDetail

class CartView(View):
    @LoginConfirm
    def post(self, request):
        try:
            data                    = json.loads(request.body)
            token                   = request.headers.get("Authorization",None)
            token_payload           = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            nickname                = Member.objects.get(nickname=token_payload['nickname'])
            now                     = datetime.now()
            ordernumber             = str(nickname.id) + "now.year" + "now.month" + "now.day" + "now.hour" + "now.minute"
            ordered_color_name      = data['name']
            ordered_quantity        = data['order_quantity']

            if Order.objects.filter(member_id=nickname.id, order_status=1).exists():
                order = Order.objects.filter(order_status=1).last()

            else:
                order = Order.objects.create(
                    order_num       = ordernumber,
                    order_status    = OrderStatus.objects.get(id=1),
                    member          = nickname
                )

            prod = OrderDetail.objects.filter(order_id=order.id)
            if prod.exists():
                prod.filter(color__name=data['name']).update(quantity=ordered_quantity)

            else:
                OrderDetail.objects.create(
                    product_id      = data['id'],
                    quantity        = ordered_quantity,
                    color_id        = Color.objects.get(name=ordered_color_name).id,
                    order_id        = order.id
                )

        except KeyError:
            return HttpResponse(status=400)
