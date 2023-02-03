class Coche:
    def __init__(self, color, matricula, cambio):
        self.color = color
        self.matricula = matricula
        self.cambio = cambio

    def __repr__(self):
        return repr((self.matricula, self.color, self.cambio))    
     
coches = [Coche('Rojo', '4859-A', 'A'), Coche('Azul', '2901-Z', 'M'), Coche('Gris', '1892-B', 'M')]
sorted(coches, key=lambda coche : coche.matricula)
[('1892-B', 'Gris', 'M'), ('2901-Z', 'Azul', 'M'), ('4859-A', 'Rojo', 'A')]