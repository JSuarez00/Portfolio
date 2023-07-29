
from django.urls import path
from miportafolio.views import home , porta

app_name="proyecto"

urlpatterns = [
    path('', home, name= 'home'),
   path('<int:proyecto_id>', porta , name="porta2")
] 
