from django.core.management.base import BaseCommand
from .models import Productos


class Command(BaseCommand):
    @staticmethod
    def add_arguments():
        for i in range(1, 51):
            producto = Productos.objects.create(
                nombre=f"Producto {i}",
                descripcion=f"Descripción del producto {i}",
                precio=i * 10  
            )
            print(f"Producto {i} creado.")

if __name__ == '__main__':
    Command.add_arguments()