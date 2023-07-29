from django.db import models
import datetime

# Create your models here.
class post(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=2000)
    imagen=models.ImageField(upload_to='block/media/images')
    link=models.URLField(None)
    
    def __str__(self):
        
        return "post: " + self.nombre
