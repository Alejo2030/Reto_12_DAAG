# Conteo de consonantes. Reto 12 
def contar_consonantes ( texto= int): # Se crea una funcion para contar las consonantes del texto 
    consonantes = 0 #Se pone un conteo que empiece desde cero que seran las consonates 
    for letra in texto: # que itere cada letra en el texto
        if letra.isalpha() and letra  not in "AEIOUaeiou": # Si la letra no es un una vocal mayuscula o minuscula, se utiliza str.isalpha para que evalue solo caractes alfabetico 
            consonantes += 1  # Sumar uno a la cuenta de vocales 
    return consonantes# Devolver consonantes 


with open( "programacion.txt" , 'r') as file: # Se abre el texto guardado con la r de read y decimos que no lo guarde como un archivo
    texto = file.read() # Que texto sea igual al archivo abierto para leer (txt)
    print( "El numero de consonantes en el texto es: " + str(contar_consonantes(texto)))   # Que imprima el numero de consonantes que se tiene en el texto llamando la función 
    print(  "El numero de consonates es "+ str(contar_consonantes("Programacion"))) # Ejemplo, imprime 7 consonantes 