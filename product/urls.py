from django.urls import path
from .views import ProductView, CategoryView

urlpatterns = [
    path('/main', ProductView.as_view()),
    path('/category/<int:category_id>',CategoryView.as_view()),
]
