class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        color = input()
        if (color == 'rojo') or (color == 'verde') or (color == 'amarillo') or (color == 'negro') or (color == 'blanco'):
            self.color = color
        else: 
            print('No es posible cambiar el color')

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        numeroAsientos = 0
        for asiento in self.asientos:
            if isinstance(Asiento):
                numeroAsientos += 1
        return (numeroAsientos)       

    def verificarIntegridad(self):
        if ((Asiento.registro == Auto.registro) and (Motor.registro == Auto.registro)):  
            return ('Auto original')
        else:
            return ('Las piezas no son originales')

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = int(input())

    def asignarTipo(self, tipo):
        valor = input()
        if (valor == 'electrico') or (valor == 'gasolina'):
            self.tipo = valor
        else: 
            self.tipo = tipo