from django.http import JsonResponse
from api.serializers import ProductSerializer,OrderSerializer
from api.models import Product,Order,OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny
)

#generic view (class based view) //this opposite to django ninja
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    #queryset=Product.objects.filter(stock__gt=0)#filtering
    serializer_class=ProductSerializer
    permission_classes = [IsAuthenticated] #only authenticated users can access this view
  
    # def get_permissions(self):
    #     self.permission_classes = [AllowAny]
    #     if self.request.method == 'POST':
    #         self.permission_classes = [IsAdminUser]
    #     return super().get_permissions()

    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    # def get_permissions(self):
    #     self.permission_classes = [AllowAny]
    #     if self.request.method in ['PUT', 'PATCH', 'DELETE']:
    #         self.permission_classes = [IsAdminUser]
    #     return super().get_permissions()  
    # 
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs) 

class OrderListAPIView(generics.ListAPIView):
    queryset=Order.objects.prefetch_related('items__product')  
    serializer_class=OrderSerializer          
  


##function based view
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    # return JsonResponse({'data':serializer.data})
@api_view(['POST'])
def add_product(request):
    # Deserialize the incoming data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # Save the new product to the database
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Return validation errors if the data is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)

