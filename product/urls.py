from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', crud, basename='user')

urlpatterns = [
    path('register', Register.as_view(),name="registration"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('create-product', CreateProductAPIView.as_view(), name="create_product"),
    path('retrieve-product/', RetrieveProductAPIView.as_view(), name="retrieve_product"),
    path('update-product/<str:id>', UpdateProductAPIView.as_view(), name="update_product"),
    path('delete-product/<str:id>', DeleteProductAPIView.as_view(), name="delete_product"),
]

urlpatterns += router.urls