def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.
    :param data: dict - diccionario a procesar.
    :return: None"""
    suma = 0
    divicion = 0
    for producto in data.keys():
        for valor in range(len(data[producto])):
            divicion +=1
            suma += data[producto][valor]
        print (f"{producto}: ventas totales ${suma:.2f}, promedio ${(suma/divicion):.2f}")
        divicion = 0
        suma = 0
