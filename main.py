from input import obtener_calificaciones
from Processing import calcular_promedio
from output import mostrar_resultado

if __name__ == "__main__":
    calificaciones = obtener_calificaciones()
    promedio = calcular_promedio(calificaciones) 
    mostrar_resultado(promedio)
