from django.urls import path
from .views import product_upload_view
from .views import product_list
from .views import product_detail
from .views import product_update_view
from .views import delete_product


urlpatterns = [
    path("products/upload/", product_upload_view, name = "product_uploadview"),
    path("products/list/", product_list, name="products_list_view"),
    path("products/<int:id>/", product_detail, name="product_detail_view"),
    path("products/edit/<int:id>/", product_update_view, name="product_update"),
    path("products/delete/<int:id>/", delete_product, name="delete_product_view"),
]