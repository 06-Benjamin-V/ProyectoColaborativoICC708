def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)