from Token import Token
from Error import Error


class Analizador:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ""
        self.estado = 0
        self.i = 0
        print("me he inicializado")
