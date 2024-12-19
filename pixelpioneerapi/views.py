from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from pixelpioneer.models import ProductCard
from pixelpioneer.serializers import ProductCardSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework_api_key.permissions import HasAPIKey

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @permission_classes([HasAPIKey])
def getAllProducts(request):
    products = ProductCard.objects.all()
    serializer = ProductCardSerializer(products, many=True)
    return Response({
        "status": True,
        "data": serializer.data
        })


@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Get products by category name",
    manual_parameters=[
        openapi.Parameter(
            'category',
            openapi.IN_QUERY,
            description="Category name to filter products",
            type=openapi.TYPE_STRING
        )
    ]
)
def getProductsByCategory(request):
    category = request.query_params.get('category', '')
    if category:
        products = ProductCard.objects.filter(category__icontains=category)
        serializer = ProductCardSerializer(products, many=True)
        return Response({
            "status": True,
            "message": f"Products in category: {category}",
            "data": serializer.data
        })
    return Response({
        "status": False,
        "message": "Category parameter is required",
    }, status=400)


@api_view(['GET'])
def getProductById(request, id):
    try:
        product = ProductCard.objects.get(id=id)
    except ProductCard.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
    
    serializer = ProductCardSerializer(product)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=ProductCardSerializer)
@api_view(['POST'])
def addProduct(request):
    serializer = ProductCardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "message": "Product created successfully",
            "data": serializer.data
        }, status=201)
    return Response({
        "status": False,
        "message": "Invalid data",
        "errors": serializer.errors
    }, status=400)


@api_view(['PUT'])
def updateProduct(request, id):
    try:
        product = ProductCard.objects.get(id=id)
        serializer = ProductCardSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except ProductCard.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

@api_view(['DELETE'])
def deleteProduct(request, id):
    try:
        product = ProductCard.objects.get(id=id)
    except ProductCard.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
    
    product.delete()
    return Response({"message": "Product deleted successfully"})