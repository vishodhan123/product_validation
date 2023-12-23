from django.urls import path
from .views import AddProductView, ProductListView

urlpatterns = [
    path('api/add_product/', AddProductView.as_view(), name='add_product'),
    path('api/list_products', ProductListView.as_view(), name='list_products'),

]
