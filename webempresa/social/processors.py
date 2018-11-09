from .models import Link

#Función de extensión del diccionario de contexto.
def extend_dic(request):
    ext = {}
    links = Link.objects.all()
    for link in links:
        ext[link.key] = link.url
    return ext