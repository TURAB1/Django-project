from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list),
    path('add_product/', views.add_product),
    path('products/',views.ProductListCreateAPIView.as_view()),
   # path('products/<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('products/<int:product_id>/',views.ProductUpdateDestroyAPIView.as_view()),
    path('orders/',views.OrderListAPIView.as_view()),


]