from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'productos/index.html')

def productos_view(request):
    categorias = {
'Frutas': ['Manzana', 'Banana', 'Pera'],
'Verduras': ['Tomate', 'Lechuga', 'Zanahoria'],
'Lácteos': ['Leche', 'Yogurt', 'Queso']
}
    return render(request, 'productos/productos.html', {'categorias': categorias})

