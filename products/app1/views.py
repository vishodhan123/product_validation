from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from .models import Product


class AddProductView(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            name = data.get('name')
            status = data.get('status')

            # validating incoming json request
            if not name or status not in ['active', 'inactive']:
                return Response({"msg": "Invalid data"}, status=http_status.HTTP_400_BAD_REQUEST)

            product = Product(name=name, status=status)
            product.save()

            return Response({
                "msg": "product added successfully",
                'uuid': str(product.uuid),
                'name': product.name,
                'status': product.status
            }, status=http_status.HTTP_201_CREATED)

        except KeyError:
            return Response({"msg": "Missing data"}, status=http_status.HTTP_400_BAD_REQUEST)


class ProductListView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all().values('uuid', 'name', 'status')
        return Response(list(products))
