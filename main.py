class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        colores = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if color in colores:
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
            if (asiento != None):
                if (asiento.registro != self.registro):
                    return 'Las piezas no son originales'
                
        if (self.motor.registro != self.registro):
            return 'Las piezas no son originales'
        
        return 'Auto original'

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        nuevoregistro = int()
        if (nuevoregistro != registro):
            registro = nuevoregistro
        
    def asignarTipo(self, tipo):
        valor = ['electrico', 'gasolina']
        if (tipo in valor):
            self.tipo = tipo
        