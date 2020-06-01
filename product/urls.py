from django.urls import path
from .views import ProductView

urlpatterns = [
    path('/main', ProductView.as_view()),
    path('category',ProductView.as_view()),
]
