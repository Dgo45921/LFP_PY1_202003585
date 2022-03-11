from Token import Token
from Error import Error
from prettytable import PrettyTable


class Analizador:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ""
        self.estado = 0
        self.i = 0

    def imprimir_tokens(self):
        x = PrettyTable()
        x.field_names = ["lexema", "linea", "columna", "tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna, token.tipo])
        print(x)

    def imprimir_errores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "linea", "columna"]
        for error in self.listaErrores:
            x.add_row([error.descripcion, error.linea, error.columna])
        print(x)

    def agrega_token(self, lexema, linea, columna, tipo):
        self.listaTokens.append(Token(lexema, linea, columna, tipo))

    def agrega_error(self, caracter, linea, columna):
        self.listaErrores.append(Error("Caracter: " + caracter + "desconocido", linea, columna))

    def q0(self, caracter):
        if caracter == "[":
            self.estado = 1
            self.buffer += caracter
            self.columna += 1

        elif caracter == "]":
            self.estado = 2
            self.buffer += caracter
            self.columna += 1

        elif caracter.isalpha():
            self.estado = 3
            self.buffer += caracter
            self.columna += 1

        elif caracter == "<":
            self.estado = 4
            self.buffer += caracter
            self.columna += 1

        elif caracter == ">":
            self.estado = 5
            self.buffer += caracter
            self.columna += 1

        elif caracter == ":":
            self.estado = 6
            self.buffer += caracter
            self.columna += 1

        elif caracter == ",":
            self.estado = 7
            self.buffer += caracter
            self.columna += 1

        elif caracter == "~":
            self.estado = 8
            self.buffer += caracter
            self.columna += 1

        elif caracter == '"':
            self.estado = 9
            self.buffer += caracter
            self.columna += 1

        elif caracter == " ":
            self.columna += 1

        elif caracter == "\n":
            self.columna = 0
            self.linea += 1

        elif caracter == "\t":
            self.columna += 8

        elif caracter == "#":
            print("fin del análisis")
        else:
            self.agrega_error(caracter, self.linea, self.columna)

    def q1(self, caracter):
        pass

    def q2(self, caracter):
        pass

    def q3(self, caracter):
        pass

    def q4(self, caracter):
        pass

    def q5(self, caracter):
        pass

    def q6(self, caracter):
        pass

    def q7(self, caracter):
        pass

    def q8(self, caracter):
        pass

    def q9(self, caracter):
        pass

    def q10(self, caracter):
        pass

    def analizar(self, cadena):
        self.listaTokens = []
        self.listaErrores = []
        self.i = 0
        cadena += "#"

        while self.i < len(cadena):
            if self.estado == 0:
                self.q0(cadena[self.i])
            elif self.estado == 1:
                self.q1(cadena[self.i])
            elif self.estado == 2:
                self.q2(cadena[self.i])
            elif self.estado == 3:
                self.q3(cadena[self.i])
            elif self.estado == 4:
                self.q4(cadena[self.i])
            elif self.estado == 5:
                self.q5(cadena[self.i])
            elif self.estado == 6:
                self.q6(cadena[self.i])
            elif self.estado == 7:
                self.q7(cadena[self.i])
            elif self.estado == 8:
                self.q8(cadena[self.i])
            elif self.estado == 9:
                self.q9(cadena[self.i])
            elif self.estado == 10:
                self.q10(cadena[self.i])
