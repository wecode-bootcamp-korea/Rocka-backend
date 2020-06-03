from django.urls import path, include

urlpatterns = [
    path('member', include('member.urls')),
    path('product',include('product.urls')),
    path('store', include('store.urls')),
]
