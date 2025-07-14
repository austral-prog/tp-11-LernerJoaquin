def process_dict(data):
    suma = 0
    divicion = 0
    for producto in data.keys():
        for valor in range(len(data[producto])):
            divicion +=1
            suma += data[producto][valor]
        print (f"{producto}: ventas totales ${suma:.2f}, promedio ${(suma/divicion):.2f}")
        divicion = 0
        suma = 0
