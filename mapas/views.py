from django.shortcuts import render
from django.http import JsonResponse
from .models import PuntoMapa, Dependencia

import json
from django.shortcuts import render
from .models import PuntoMapa, Dependencia

def mapa_view(request):
    dependencias = Dependencia.objects.prefetch_related('subcategorias').all()

    # Defines tus colores por colonia aquí en la vista

    
# En tu views.py
    colores_colonias = {
        "El Chaparral": "#4d4383",           # morado-oscuro
        "Rinconada de Atizapán": "#6767a5",  # morado-claro
        "Las Huertas": "#56858d",            # verde-azulado
        "Rancho Los Rojas": "#79b0cc",       # azul-claro
        "Zona Industrial II México": "#b64f80", # magenta
        "Relleno Sanitario": "#585958",      # gris-oscuro
        "Ejido Espiritu Santo": "#0f1f3d",   # azul-noche
        "San José El Jaral I": "#4d4383",    # repites morado-oscuro
        "México Nuevo": "#56858d"            # repites verde-azulado
    }

    # Pasamos los colores como JSON al template
    context = {
        'dependencias': dependencias,
        'colores_colonias_json': json.dumps(colores_colonias)
    }
    return render(request, 'mapas/index.html', context)

def get_puntos(request):
    puntos = PuntoMapa.objects.select_related('subcategoria', 'subcategoria__dependencia').all()
    
    data = []
    for p in puntos:
        data.append({
            'nombre': p.nombre,
            'latitud': float(p.latitud),
            'longitud': float(p.longitud),
            'dependencia': p.subcategoria.dependencia.nombre, 
            'subcategoria': p.subcategoria.nombre,
            'subcategoria_id': p.subcategoria.id, # ¡NUEVO! Agregamos el ID de la subcategoría
            'color': p.subcategoria.color_marcador,
            'descripcion': p.descripcion
        })
        
    return JsonResponse({'puntos': data}, safe=False)