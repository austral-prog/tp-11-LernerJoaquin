def read_file_to_dict(nombre_archivo):
    ventas_por_producto = {}

    try:
        archivo = open(nombre_archivo, 'r')
        linea = archivo.readline().strip()
        archivo.close()

        if linea == "":
            print("El archivo está vacío.")
            return {}

        ventas = linea.split(';')
        for venta in ventas:
            if venta != "":
                partes = venta.split(':')
                if len(partes) == 2:
                    producto = partes[0]
                    valor = float(partes[1])
                    if producto in ventas_por_producto:
                        ventas_por_producto[producto].append(valor)
                    else:
                        ventas_por_producto[producto] = [valor]
                else:
                    print("Venta mal formateada:", venta)

    except FileNotFoundError:
        print("El archivo no existe.")
        return {}
    except:
        print("Ocurrió un error al leer el archivo.")
        return {}

    return ventas_por_producto

def process_dict(diccionario):
    for producto in diccionario:
        montos = diccionario[producto]
        total = 0
        for monto in montos:
            total = total + monto
        promedio = total / len(montos)
        print(producto + ": ventas totales $" + str(round(total, 2)) + ", promedio $" + str(round(promedio, 2)))
