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
        self.buffer = ""

    def agrega_error(self, caracter, linea, columna):
        self.listaErrores.append(Error("Caracter: " + caracter + " desconocido", linea, columna))

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

        elif caracter == "'":
            self.estado = 11
            self.buffer += caracter
            self.columna += 1

        elif caracter == " ":
            self.columna += 1

        elif caracter == "\n":
            self.columna = 0
            self.linea += 1

        elif caracter == "\t":
            self.columna += 8

        elif caracter == "$":
            print("fin del análisis")
        else:
            self.agrega_error(caracter, self.linea, self.columna)

    def q1(self):
        self.agrega_token(self.buffer, self.linea, self.columna, "Corchete izquierdo")
        self.estado = 0
        self.i -= 1

    def q2(self):
        self.agrega_token(self.buffer, self.linea, self.columna, "Corchete derecho")
        self.estado = 0
        self.i -= 1

    def q3(self, caracter):
        if caracter.isalpha():
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        else:
            if self.buffer in ["tipo", "valor", "fondo", "valores", "nombre", "evento", "formulario"]:
                self.agrega_token(self.buffer, self.linea, self.columna, "Palabra reservada_" + self.buffer)
                self.estado = 0
                self.i -= 1
            else:
                self.agrega_token(self.buffer, self.linea, self.columna, "Identificador")
                self.estado = 0
                self.i -= 1

    def q4(self):
        self.agrega_token(self.buffer, self.linea, self.columna, "Signo menor")
        self.estado = 0
        self.i -= 1

    def q5(self):
        self.agrega_token(self.buffer, self.linea, self.columna, "Signo mayor")
        self.estado = 0
        self.i -= 1

    def q6(self):
        self.agrega_token(self.buffer, self.linea, self.columna, "Signo dos puntos")
        self.estado = 0
        self.i -= 1

    def q7(self):
        self.agrega_token(self.buffer, self.linea, self.columna, "Coma")
        self.estado = 0
        self.i -= 1

    def q8(self):
        self.agrega_token(self.buffer, self.linea, self.columna, "Virgulilla")
        self.estado = 0
        self.i -= 1

    def q9(self, caracter):
        if caracter != '"':
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 10
            self.i -= 1

    def q10(self, caracter):
        self.buffer += caracter
        self.columna += 1
        self.agrega_token(self.buffer, self.linea, self.columna, "valor string")
        self.estado = 0

    def q11(self, caracter):
        if caracter != "'":
            self.estado = 11
            self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 12
            self.i -= 1

    def q12(self, caracter):
        self.buffer += caracter
        self.columna += 1
        self.agrega_token(self.buffer, self.linea, self.columna, "valor string")
        self.estado = 0

    def analizar(self, cadena):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.i = 0
        cadena += "$"

        while self.i < len(cadena):
            if self.estado == 0:
                self.q0(cadena[self.i])
            elif self.estado == 1:
                self.q1()
            elif self.estado == 2:
                self.q2()
            elif self.estado == 3:
                self.q3(cadena[self.i])
            elif self.estado == 4:
                self.q4()
            elif self.estado == 5:
                self.q5()
            elif self.estado == 6:
                self.q6()
            elif self.estado == 7:
                self.q7()
            elif self.estado == 8:
                self.q8()
            elif self.estado == 9:
                self.q9(cadena[self.i])
            elif self.estado == 10:
                self.q10(cadena[self.i])
            elif self.estado == 11:
                self.q11(cadena[self.i])
            elif self.estado == 12:
                self.q12(cadena[self.i])
            self.i += 1
