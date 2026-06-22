def porcentaje_vida(actual, maxima):
    porcentaje= actual / maxima * 100
    return porcentaje


def estado_vida(porcentaje):
    if porcentaje <= 25:
        devolver="CRITICO"
    elif porcentaje <= 50:
        devolver="HERIDO"
    else:
        devolver="SANO"
    return devolver


def comprar_pociones(monedas, precio):
    cantidad = monedas // precio
    vuelto = monedas % precio
    return cantidad, vuelto
 
