from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name')
        price = self.request.query_params.get('price')
        if name is not None and price is not None:
            queryset = queryset.filter(name__icontains=name, price=price) 
        elif name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif price is not None:
            queryset = queryset.filter(price=price)
        return queryset
