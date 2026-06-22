def nombre_usuario(nombre):
    if len(nombre)>=3 and nombre.isalpha():
        devolver=True
    else:
        devolver=False
    return devolver 
def crea_codename(nombre, nivel):
    if nombre[:4].upper()+ "-Lv" + str(nivel):
        print(nombre, nivel)
    return codename
def vida_maxima(nivel):
    r=100+nivel**2*5
    return r


nombre="pachu"
print(nombre_usuario(nombre))
print(crea_codename(nombre,100))

