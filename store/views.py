import json
import jwt

from django.http import  JsonResponse
from django.shortcuts import render
from django.views import View

from .models import Store

class StoreView(View):
    def get(self, request):
        all_store = Store.objects.all()
        stores=[{
            'name'          : store.name,
            'branch'          : store.branch,
            'phone_number'           : store.phone_number,
            'address'       : store.address,
            'store_time'       : store.store_time,
            'map_url'           : store.map_url
        } for store in all_store]
        return JsonResponse({'data':stores}, status=200)
