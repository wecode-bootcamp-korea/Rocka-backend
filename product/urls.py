from django.urls import path
from .views import ProductView

urlpatterns = [
    path('/main', ProductView.as_view()),
]
