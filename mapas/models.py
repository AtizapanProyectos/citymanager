from django.db import models

# 1. LA DEPENDENCIA PRINCIPAL (Para crear los acordeones morados)
class Dependencia(models.Model):
    nombre = models.CharField(max_length=100, unique=True) # Ej: DIF, Educación, SAPASA

    def __str__(self):
        return self.nombre

# 2. LAS ÁREAS / SUBCATEGORÍAS (Para crear las listas con checkboxes y colores)
class Subcategoria(models.Model):
    nombre = models.CharField(max_length=100) # Ej: Estancias Infantiles, Becas
    # Relacionamos esta subcategoría con una Dependencia
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE, related_name='subcategorias')
    # El color ahora va aquí, porque cada área tiene su propio color
    color_marcador = models.CharField(max_length=20, default='#4d4383') 

    def __str__(self):
        return f"{self.nombre} ({self.dependencia.nombre})"

# 3. LOS PUNTOS EN EL MAPA (Las coordenadas reales)
class PuntoMapa(models.Model):
    nombre = models.CharField(max_length=200) # Ej: Estancia Infantil "Margarita Maza"
    # Relacionamos el punto directo a la subcategoría
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, related_name='puntos')
    
    latitud  = models.DecimalField(max_digits=21, decimal_places=17)
    longitud = models.DecimalField(max_digits=22, decimal_places=17)  
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.subcategoria.nombre}"