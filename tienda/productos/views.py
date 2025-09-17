from django.http import JsonResponse
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all().values("id", "nombre", "precio", "stock", "disponible")
    return JsonResponse(list(productos), safe=False)

def detalle_producto(request, producto_id):
    try:
        producto = Producto.objects.values("id", "nombre", "precio", "stock", "disponible").get(id=producto_id)
        return JsonResponse(producto)
    except Producto.DoesNotExist:
        return JsonResponse({"error": "Producto no encontrado"}, status=404)