from django.shortcuts import render, get_object_or_404
from miportafolio.models import proyecto
# Create your views here.


def home(request):
    projects=proyecto.objects.all()
    
    return render(request ,"index.html", {"projects":projects} )

def porta(request, proyecto_id):
    portar=get_object_or_404(proyecto, pk=proyecto_id )
    
    return render(request, 'proyecto.html', {"proyecto":portar})

