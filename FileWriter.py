from os import system


def crear_html(lista_elementos, texto_archivo):
    pagina = open("Formulario.html", "w")
    pagina.write("<!DOCTYPE html>")
    pagina.write("\n")
    pagina.write("<html>")
    pagina.write("\n")
    pagina.write("<h2>Formulario generado:</h2>")
    pagina.write("\n")

    pagina.write("<form>\n")

    for elemento in lista_elementos:
        if elemento["tipo"] == "etiqueta":
            pagina.write("<label>" + elemento["valor"] + "</label><br>")
            pagina.write("\n")

        elif elemento["tipo"] == "texto":
            pagina.write("""<input type="text" name="texto" """ + " placeholder=" + '"' + elemento[
                "fondo"] + '"' + " value=" + '"' + elemento["valor"] + '"><br><br><br>')
            pagina.write("\n")

        elif elemento["tipo"] == "grupo-radio":
            pagina.write("<label>" + elemento["nombre"] + "</label><br>")
            for i in range(len(elemento["valores"])):
                pagina.write(
                    """<input type="radio" """ + """ name="radio" value=""" + '"' + elemento["valores"][i] + '"' + ">")
                pagina.write("\n")
                pagina.write(
                    "<label" + " for=" + '"' + elemento["valores"][i] + '">' + elemento["valores"][i] + """</label>""")
                pagina.write("\n")

            pagina.write("<br><br><br>")

        elif elemento["tipo"] == "grupo-option":

            pagina.write("<label for = " + '"' + elemento["nombre"] + '">' + elemento["nombre"] + " " + "</label>")
            pagina.write("<select name = " + '"' + elemento["nombre"] + '">')
            pagina.write("\n")
            for i in range(len(elemento["valores"])):
                pagina.write("<option>" + elemento["valores"][i] + "</option>")
                pagina.write("\n")
            pagina.write("</select>")

            pagina.write("<br><br><br>")

        elif elemento["tipo"] == "boton":
            if elemento["evento"] == "info":
                pagina.write("""<button type = "button" id = "info"> """ + elemento["valor"] + "</button>")
            elif elemento["evento"] == "entrada":
                pagina.write("""<button type = "button" id = "entrada"> """ + elemento["valor"] + "</button>")

    pagina.write("</form>\n")
    pagina.write("\n")

    pagina.write("""<script src = "https://code.jquery.com/jquery-3.6.0.min.js"></script> """)
    pagina.write(""" <script>
    
    
    $(document).ready(function() {
    $("#info").click(function(){
    console.log("hey yo soy info")
     
        
        $('#serializearray').text(        
            array = ($('form').serializeArray())
            
        );
        console.log(array)
        var cadena = ""
        for (let step = 0; step < array.length; step++) {
        cadena = cadena + array[step].value + "<br>"
}
			
    var element = document.getElementById("ifrm");

    if(typeof(element) != 'undefined' && element != null){
        document.getElementById('ifrm').src = "data:text/html;charset=utf-8," + cadena;
    } else{
        var ifrm = document.createElement('iframe');
		ifrm.setAttribute('id', 'ifrm');
		document.body.appendChild(ifrm); 
    document.getElementById('ifrm').src = "data:text/html;charset=utf-8," + cadena;
    }
				
        
   
    }); 
    
    
    
    
    $("#entrada").click(function(){
    console.log("hey yo soy entrada")
    var element = document.getElementById("ifrm");
        
        if(typeof(element) != 'undefined' && element != null){
        element.setAttribute("width", "1000px")
		element.setAttribute("height", "500px")
		element.open()
        element.close()
        element.contentDocument.write(""" + "`" + texto_archivo + "`)"  """          
    } else{
        var ifrm = document.createElement('iframe');
		ifrm.setAttribute('id', 'ifrm');
		ifrm.setAttribute("width", "1000px")
		ifrm.setAttribute("height", "500px")
		document.body.appendChild(ifrm); 
    ifrm.contentDocument.write(""" + "`" + texto_archivo + "`)"  """ 
    }
        
    }); 
    
});



    

    """ + """ </script>""")

    pagina.write("</body>")
    pagina.write("\n")
    pagina.write("</html>")

    pagina.close()
    system("firefox Formulario.html")


def reporte_tokens(lista_tokens):
    reporte = open("Reporte_tokens.html", "w")
    reporte.write("<!DOCTYPE html>\n")
    reporte.write("<html>\n")
    reporte.write("<head>\n")
    reporte.write("""<meta charset="UTF-8">\n""")
    reporte.write("<title>reporte de tokens</title>\n")
    reporte.write("""<link rel="stylesheet" href="style.css">\n""")
    reporte.write("</head>\n")
    reporte.write("<body>\n")
    reporte.write("<h1>Reporte de tokens</h1>")
    # aqui ira la tabla
    reporte.write("<table>\n")
    reporte.write("<tr>\n")
    reporte.write("<th>Lexema</th>\n")
    reporte.write("<th>Linea</th>\n")
    reporte.write("<th>Columna</th>\n")
    reporte.write("<th>Tipo</th>\n")
    reporte.write("</tr>\n")
    for token in lista_tokens:

        reporte.write("<tr>")
        reporte.write("<td>" + token.lexema + "</td>")
        reporte.write("<td>" + str(token.linea) + "</td>")
        reporte.write("<td>" + str(token.columna) + "</td>")
        reporte.write("<td>" + token.tipo + "</td>")
        reporte.write("</tr>")


    reporte.write("</table>")
    reporte.write("</body>\n")
    reporte.write("</html>\n")
    reporte.close()
    system("firefox Reporte_tokens.html")


def reporte_errores(lista_errores):
    reporte = open("Reporte_errores.html", "w")
    reporte.write("<!DOCTYPE html>\n")
    reporte.write("<html>\n")
    reporte.write("<head>\n")
    reporte.write("""<meta charset="UTF-8">\n""")
    reporte.write("<title>reporte de errores</title>\n")
    reporte.write("""<link rel="stylesheet" href="style.css">\n""")
    reporte.write("</head>\n")
    reporte.write("<body>\n")
    reporte.write("<h1>Reporte de errores</h1>")
    # aqui ira la tabla
    reporte.write("<table>\n")
    reporte.write("<tr>\n")
    reporte.write("<th>Descripcion</th>\n")
    reporte.write("<th>Linea</th>\n")
    reporte.write("<th>Columna</th>\n")
    reporte.write("</tr>\n")
    for error in lista_errores:
        reporte.write("<tr>")
        reporte.write("<td>" + error.descripcion + "</td>")
        reporte.write("<td>" + str(error.linea) + "</td>")
        reporte.write("<td>" + str(error.columna) + "</td>")
        reporte.write("</tr>")

    reporte.write("</table>")
    reporte.write("</body>\n")
    reporte.write("</html>\n")
    reporte.close()
    system("firefox Reporte_errores.html")
