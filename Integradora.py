#Parte A
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

#Parte B
def clasificar_arma(opcion_menu):
    if opcion_menu==1:
        return"Legendaria"
    elif opcion_menu==2:
        return"Media"
    else:return"Debil"
def es_critico(es_magica,nivel):
    return es_magica or nivel>=10
def danio_base(ataque, poder,defensa):
    return(ataque+poder)-defensa
def danio_total(ataque,poder,defensa,critico):
    base=danio_base(ataque,poder,defensa)
    if critico==True:
        return base*2
    else:
        return base
print("1-escopeta")
print("2-espada")
print("3-tirachinas")
opcion_elegida=int(input("Escriba el numero de su arma:"))
if opcion_elegida==1:
    es_magica=True
else:
    es_magica=False
nivel=0
if opcion_elegida==1:
    poder=50
elif opcion_elegida==2:
    poder=25
else:
    poder=5
ataque=40
defensa=15
resultado_arma=clasificar_arma(opcion_elegida)
resultado_critico=es_critico(es_magica,nivel)
danio_base_calculado=danio_base(ataque,poder,defensa)
danio_final=danio_total(ataque,poder,defensa,resultado_critico)
print("El poder que tiene tu arma es:",resultado_arma)
print("¿El golpe es critico?:",resultado_critico)
print("El daño BASE realizado es:",
      danio_base_calculado)
print("El daño total realizado es:", danio_final)

#Parte C
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
#Parte D
def puede_atacar(energia, esta_aturdido):
    if energia>0 and not esta_aturdido:
        devolver=True
    else:
        devolver=False
    return devolver
def vida_restante(vida, dano):
    if vida-dano<0:
       devolver= 0
    else:
        devolver= vida - dano
    return devolver
def gana(vida_heroe, vida_enemigo):
    if vida_heroe >0 and vida_enemigo<=0:
       devolver=True
    else:
        devolver=False
    return devolver

main()
int(input("Decime un nombre")

 
