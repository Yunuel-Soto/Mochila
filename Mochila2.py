#Mejorado
class mochilaArti:
    def __init__ (self, peso, valor, indice):
        self.indice = indice
        self.peso = peso
        self.valor = valor
    def __repr__ (self):
        return repr((self.peso, self.valor, self.indice))

def getMaxValue(peso, valor, capacidad):
    mochila = []
    p = len(peso)
    indice = 0 
    for i in range(p):
        indice = peso[i] / valor[i]
        mochila.append(mochilaArti(peso[i], valor[i], indice))
        
    mochila.sort(key=lambda mochila:mochila.indice)
    # mochila.reverse()
    cont = 0


    for object in mochila:
        actualPeso = int (object.peso)
        actualValor = int (object.valor)
        if ((capacidad - actualPeso) >= 0):
            capacidad = capacidad - actualPeso
            cont = cont + actualValor
    return cont

peso = [1,2,3]
valor = [100,10,30]
capacidad = 4
maxValue = getMaxValue(peso,valor,capacidad)

print('Valor maximo en la mochila es: ', maxValue)