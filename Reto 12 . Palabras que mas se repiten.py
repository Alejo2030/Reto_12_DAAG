#Palabras que mas se repiten. Reto 12 
def palabrasRepetidas(texto:str):
    
    texto = texto.lower() #Pasar las letras del texto a minusculas 
    nPalabras = {} # Diccionario vacio que contendra las palabras mas repetidas y el numero de veces que estan se ven en el texto 

    for s in texto: 
        if not s.isalpha() and s != " ": # Covierte los signos que no sean de alfabeto en espacios 
            texto =  texto.replace(s, " ")

    narchivo = texto.split() # Separar las palabras por espacios y saltos de linea 

    for l in narchivo: nPalabras[l] = 0 # Ciclo for que inicializa las palabras repetidas del texto en el diccionario en 0
    for l in narchivo: nPalabras[l] += 1 # Ciclo for que obtiene las palabras repetidas y aumenta en uno la cantidad de apariciones de la misma en el texto

    for s in sorted(nPalabras, reverse=True, key= lambda s: nPalabras[s])[:51]: # Ordena las palabras por el numero de aparicones en el texto de manera descendiene
        print("La palabra {} se repite {} veces en el texto".format(s, nPalabras[s]))  # Impresión del resultado usando el metodo .format



with open( "programacion.txt" , 'r') as file: # Se abre el texto guardado con la r de read y decimos que no lo guarde como un archivo
    txt = file.read() # Que texto sea igual al archivo abierto para leer (txt)
    print((palabrasRepetidas(txt)))
    