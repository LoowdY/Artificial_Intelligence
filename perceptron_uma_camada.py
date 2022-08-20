



entradas = [ 2, 8 ,1]
pesos = [0.8, 0.3, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        s += e[i] * p[i]
        return s
    
s = soma(entradas, pesos)


def stepFunction(soma):
    if( soma>=1 ):
        return 1
    return 0

r = stepFunction(s)