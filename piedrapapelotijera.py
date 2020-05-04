respuesta='si'     #inicio asumiendo que quieren jugar...
while respuesta=='si':     #entro en el loop externo
    opciones=['piedra','papel','tijera']    #creo la lista para la IA
    
    import random     #importo el modulo random
    manoIA=random.choice(opciones)     #genero una eleccion de la IA random

    jugadora=input('Cual vas a jugar? Piedra, papel o tijera? ')  #que juega?
    jugadora=jugadora.lower() #convierto a minuscula para no considerar mayus
    while jugadora!='piedra' and jugadora!='papel' and jugadora!='tijera':
        jugadora=input('Porfa, ingresá "piedra", "papel" o "tijera": ')

    print()
    print('Listo?')
    print('Piedra...')
    print('Papel...')     #interaccion con el usuario
    input('O TIJERA!')
    print()
    print('Yo saqué',manoIA)
    
    if manoIA=='piedra':    #aca comienzan los outcomes según lo que sacó la IA
        if jugadora=='piedra':
            print('Es un empate! La proxima define.')
        if jugadora=='papel':
            print('GANASTE! Papel le gana a piedra. Juguemos de nuevo!')
        if jugadora=='tijera':
            print('Perdiste! La buena piedra, nada le gana. Vamos de nuevo!')
    if manoIA=='papel':
        if jugadora=='piedra':
            print('Perdiste y yo gané, yo gané. Otra?')
        if jugadora=='papel':
            print('Es un empate. Copion! Desempate YA.')
        if jugadora=='tijera':
            print('GANASTE! Buena estrategia en tiempo real. Quiero mi revancha.')
    if manoIA=='tijera':
        if jugadora=='piedra':
            print('GANASTE! No me aburro de pifiar. Otra partida?')
        if jugadora=='papel':
            print('L de LOSER! Soy una maquina con habilidades. Otra?')
        if jugadora=='tijera':
            print('Es un empate. Pensas como maquina, bien ahi, maquina.')
    respuesta=input('Queres jugar de nuevo? (si/no): ')   #vuelve el loop?
print()
print('Adios, vaquere.')    #el usuario respondio que no
print()
input('ENTER para terminar diria marito.')