#Listado de destinatarios con cantidad de mensajes recibidos. Reto 12 

def destino(texto:str): #definir la funcion destino, con variable texto la cual es un string 
    palabra  = texto.split() # Hacer lista de trings con las palabras 
    destinatario = {} # Diccionario que contiene la dirreccion de email y los mensajes enviados a esta misma 
    for i in range(len(palabra)):
        if ([i] == "by" or palabra[i] == "BY") and "." in palabra[i-1]: # El string que esta en fente de BY o by contien un destinatario 
            if palabra[i+1] in destinatario: # Se bloquea el codigo para llenar el diccionario 
                destinatario[palabra[i+1]] += 1
            else:
                destinatario[palabra[i+1]] = 1  

    listado = list(destinatario.items()) # Lista de tuplas que contiene el destinatario y los mensajes dados a el 

    return listado
    
    
with open("programacion.txt", "r") as file: #  Se abre el texto guardado con la r de read y decimos que no lo guarde como un archivo
        nombre = destino (file.read())
        for i in range(len(nombre)):
            lenstr = len(nombre[i])
            print(*nombre[i], sep=(4*" "),end="\n") #Imprime el destinatario y el nuemro de mensajes que se le han enviado separado por 4 espacios 