#Cantidad de mensajes enviados por cada día.Reto 12 

def contar_mensajes_diarios(texto: str):
    mensaje = []  # Lista para almacenar informacion con datos de fecha 
    palabras = texto.split()  # Separar las palabras del texto 

    for i in range(len(palabras)):
        if palabras[i] == "Received:":  
            segmento = []
            while palabras[i] != "-0500" and palabras[i] != "(GMT)": # Lista de palabras desde "Received" hasta "(GMT)" o "-0500".
                segmento.append(palabras[i])
                i += 1
            mensaje.append(segmento)

    msg_dia = {}  # Diccionario que contien el dia y el numero de mensajes enviados 

    for segmento in mensaje:
        indice = segmento.index('Jan')  # Índice de la palabra "Jan".
        dia = int(segmento[indice - 1])  # Extraer el día basado en el índice de "Jan".
        if dia in msg_dia:
            msg_dia[dia] += 1
        else:
            msg_dia[dia] = 1

    return msg_dia


with open("programacion.txt", "r") as file:
        msg_dia = contar_mensajes_diarios(file.read())
        for dia in msg_dia:
            print(f"Se enviaron {msg_dia[dia]} mensajes enviados el {dia} de enero, 2008")

