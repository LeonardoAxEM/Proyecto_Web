from django.db import models

class Practicas(models.Model):
    nombre = models.CharField(max_length=50)
    objetivo = models.CharField(max_length=100)
    contenido_html = models.TextField()


