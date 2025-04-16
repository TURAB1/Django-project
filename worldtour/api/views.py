from django.http import JsonResponse
from api.serializers import ProductSerializer
from api.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    # return JsonResponse({'data':serializer.data})