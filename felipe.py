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

print(puede_atacar(100,True))
print(vida_restante(60, 80))
print(gana(100,0))
