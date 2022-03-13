import FileWriter

inicio_encontrado = False
final_encontrado = False

lista_diccionarios = []
texto_archivo = ""


def hallar_elemento(lista_tokens):
    global inicio_encontrado, final_encontrado, lista_diccionarios
    lista_diccionarios = []

    indice_primero = 0
    indice_final = 0
    for i in range(len(lista_tokens)):
        if lista_tokens[i].lexema == "<" and not inicio_encontrado:
            indice_primero = i
            inicio_encontrado = True

        if lista_tokens[i].lexema == ">" and not final_encontrado and inicio_encontrado:
            indice_final = i
            final_encontrado = True

        if inicio_encontrado and final_encontrado:
            filtrar_tipo(lista_tokens[indice_primero + 1:indice_final])
            inicio_encontrado = False
            final_encontrado = False


    FileWriter.crear_html(lista_diccionarios, texto_archivo)





def filtrar_tipo(sublista):
    tipo = ""
    for i in range(len(sublista)):
        if sublista[i].lexema == "tipo" and sublista[i + 1].lexema == ":":
            tipo = sublista[i + 2].lexema

    tipo = tipo.replace('"', "")
    if tipo == "etiqueta":
        tipo_etiqueta(sublista)
    elif tipo == "texto":
        tipo_texto(sublista)
    elif tipo == "grupo-radio":
        tipo_grupo_radio(sublista)
    elif tipo == "grupo-option":
        tipo_grupo_opcion(sublista)
    elif tipo == "boton":
        tipo_boton(sublista)


def tipo_etiqueta(sublista):
    global lista_diccionarios
    valor = ""
    for i in range(len(sublista)):
        if sublista[i].lexema == "valor" and sublista[i + 1].lexema == ":":
            valor = sublista[i + 2].lexema
    valor = valor.replace("'", "").replace('"', "")
    nuevo_diccionario = {"tipo": "etiqueta", "valor": valor}
    lista_diccionarios.append(nuevo_diccionario)
    # print(lista_diccionarios)


def tipo_texto(sublista):
    global lista_diccionarios
    valor = ""
    fondo = ""
    for i in range(len(sublista)):
        if sublista[i].lexema == "valor" and sublista[i + 1].lexema == ":":
            valor = sublista[i + 2].lexema
    valor = valor.replace("'", "").replace('"', "")

    for i in range(len(sublista)):
        if sublista[i].lexema == "fondo" and sublista[i + 1].lexema == ":":
            fondo = sublista[i + 2].lexema
    fondo = fondo.replace("'", "").replace('"', "")

    nuevo_diccionario = {"tipo": "texto", "valor": valor, "fondo": fondo}
    lista_diccionarios.append(nuevo_diccionario)
    # print(lista_diccionarios)


def tipo_grupo_radio(sublista):
    global lista_diccionarios
    nombre = ""
    indice_corchete_inicial = 0
    indice_corchete_final = 0
    valores = []

    for i in range(len(sublista)):
        if sublista[i].lexema == "nombre" and sublista[i + 1].lexema == ":":
            nombre = sublista[i + 2].lexema
    nombre = nombre.replace("'", "").replace('"', "")

    for i in range(len(sublista)):
        if sublista[i].lexema == "[":
            indice_corchete_inicial = i
            break

    for i in range(len(sublista)):
        if sublista[i].lexema == "]":
            indice_corchete_final = i
            break

    lista_valores = sublista[indice_corchete_inicial + 1:indice_corchete_final]

    for token in lista_valores:
        if token.lexema == ",":
            lista_valores.remove(token)

    for i in range(len(lista_valores)):
        valores.append(lista_valores[i].lexema.replace("'", "").replace('"', ""))

    nuevo_diccionario = {"tipo": "grupo-radio", "nombre": nombre, "valores": valores}
    lista_diccionarios.append(nuevo_diccionario)
    #print(lista_diccionarios)


def tipo_grupo_opcion(sublista):
    global lista_diccionarios
    nombre = ""
    indice_corchete_inicial = 0
    indice_corchete_final = 0
    valores = []

    for i in range(len(sublista)):
        if sublista[i].lexema == "nombre" and sublista[i + 1].lexema == ":":
            nombre = sublista[i + 2].lexema
    nombre = nombre.replace("'", "").replace('"', "")

    for i in range(len(sublista)):
        if sublista[i].lexema == "[":
            indice_corchete_inicial = i
            break

    for i in range(len(sublista)):
        if sublista[i].lexema == "]":
            indice_corchete_final = i
            break

    lista_valores = sublista[indice_corchete_inicial + 1:indice_corchete_final]

    for token in lista_valores:
        if token.lexema == ",":
            lista_valores.remove(token)

    for i in range(len(lista_valores)):
        valores.append(lista_valores[i].lexema.replace("'", "").replace('"', ""))

    nuevo_diccionario = {"tipo": "grupo-option", "nombre": nombre, "valores": valores}
    lista_diccionarios.append(nuevo_diccionario)
    print(lista_diccionarios)


def tipo_boton(sublista):
    global lista_diccionarios
    valor = ""
    evento = ""
    for i in range(len(sublista)):
        if sublista[i].lexema == "valor" and sublista[i + 1].lexema == ":":
            valor = sublista[i + 2].lexema
    valor = valor.replace("'", "").replace('"', "")

    for i in range(len(sublista)):
        if sublista[i].lexema == "evento" and sublista[i + 1].lexema == ":":
            evento = sublista[i + 2].lexema
    evento = evento.replace("'", "").replace('"', "")

    nuevo_diccionario = {"tipo": "boton", "valor": valor, "evento": evento}
    lista_diccionarios.append(nuevo_diccionario)
