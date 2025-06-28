def read_file_to_dict(nombre_archivo):
    ventas_por_producto = {}

    try:
        with open(nombre_archivo, 'r') as archivo:
            linea = archivo.readline().strip()
            if not linea:
                print("El archivo está vacío.")
                return {}

            ventas = linea.split(';')

            for venta in ventas:
                if venta:  # Ignora cadenas vacías
                    try:
                        producto, valor = venta.split(':')
                        valor = float(valor)
                        if producto in ventas_por_producto:
                            ventas_por_producto[producto].append(valor)
                        else:
                            ventas_por_producto[producto] = [valor]
                    except ValueError:
                        print(f"Error de formato en la venta: {venta}")
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
        return {}

    return ventas_por_producto


def process_dict(diccionario_ventas):
    for producto, montos in diccionario_ventas.items():
        total = sum(montos)
        promedio = total / len(montos) if montos else 0
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

archivo = input("Ingrese el nombre del archivo de ventas: ")

ventas_dict = read_file_to_dict(archivo)

if ventas_dict:
    process_dict(ventas_dict)
