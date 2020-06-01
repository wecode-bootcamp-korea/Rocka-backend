from django.urls import path, include

urlpatterns = [
    path('member', include('member.urls')),
]
