def obtener_calificaciones():
    try:
        calificaciones = list(map(float, input("Ingrese las calificaciones separadas por espacio: ").split()))
        return calificaciones
    except ValueError:
        print("Error: Ingrese solo números válidos.")
        return obtener_calificaciones()