from .models import Category

#Para poder pasar la category a todos los templates de manera elegante
def ctx_category(request):
    return {'categories': Category.objects.all()}



