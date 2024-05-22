from .models import Productos
from .serializers import ProductoSerializer
from rest_framework import generics, pagination


class ListaProductos(generics.ListAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 10