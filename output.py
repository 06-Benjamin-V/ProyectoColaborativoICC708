def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0  # Evita divisiones por cero
    return sum(calificaciones) / len(calificaciones)