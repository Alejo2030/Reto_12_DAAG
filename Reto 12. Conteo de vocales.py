# Conteo de vocales. reto 12 
def contar_vocales (texto=str): # Se crea una funcion para contar las vocales del texto 
    vocales = 0 # Se pone un conteo que empiece desde cero que seran las vocales 
    for letras in texto: # que itere cada letra en el texto 
        if letras in "aeiouAEIOU": # Si una letra en el texto es una vocal minuscula  o mayuscula 
            vocales +=1 # Sumar 1 al conteo 
    return vocales # Devolver el numero de vocales 

with open( "programacion.txt" , 'r') as file: # Se abre el texto guardado con la r de read y decimos que no lo guarde como un archivo
    texto = file.read() # Que texto sea igual al archivo abierto para leer (txt)
    print( "El numero de vocales en el texto es :" + str(contar_vocales(texto))) # Que imprima el numero de vocales que se tiene en el texto llamando la función 
    print(  "El numero de vocales es "+ str(contar_vocales("Programacion"))) # Ejemplo, imprime 5 vocales 
    