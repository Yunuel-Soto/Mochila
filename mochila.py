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
    for i in range(p):
        mochila.append(mochilaArti(peso[i], valor[i], i))
        
    mochila.sort(key=lambda mochila:mochila.peso)
    mochila.reverse()
    cont = 0

    for object in mochila:
        actualPeso = int (object.peso)
        actualValor = int (object.valor)
        if ((capacidad - actualPeso) >= 0):
            capacidad = capacidad - actualPeso
            cont = cont + actualValor
    return cont

peso = [1,2,3]
valor = [10,20,30]
capacidad = 4
maxValue = getMaxValue(peso,valor,capacidad)

print('Valor maximo en la mochila es: ', maxValue)