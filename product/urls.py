from django.urls import path
from .views import ProductView, CategoryView, DetailView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/category',CategoryView.as_view()),
    path('/<int:product_id>',DetailView.as_view()),
]
