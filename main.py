class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        color = str(input())
        if (color == 'rojo') or (color == 'verde') or (color == 'amarillo') or (color == 'negro') or (color == 'blanco'):
            self.color = color

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
            if isinstance(asiento, Asiento):
                numeroAsientos += 1
        return numeroAsientos      

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if (asiento != None) and (asiento.registro != self.registro) and (self.motor.registro != self.registro):
                return 'Las piezas no son originales'
        else:
            return 'Auto original'

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        nuevo_registro = int(input())
        if (nuevo_registro != registro):
            self.registro = nuevo_registro
        return self.registro
    
    def asignarTipo(self, tipo):
        valor = str(input())
        if (valor == 'electrico') or (valor == 'gasolina'):
            self.tipo = valor
        else: 
            self.tipo = tipo