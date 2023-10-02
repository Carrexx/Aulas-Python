"""
args - Argumento não nomeado
* - * (empacotamento e desempacotamento)
"""


def soma(*args):
    total = 0
    for numero in args:
        print('total', total,'numero:', numero)
        total = total + numero
    #return total
    args = list(args)
    print('total:', total,'numero:', numero)#(args, type(args))

soma(1, 2, 3, 4, 5, 6)