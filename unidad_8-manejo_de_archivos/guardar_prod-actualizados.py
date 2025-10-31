## 6 GUARDAR PRODUCTOS ACTUALIZADOS ##

NOMBRE_ARCHIVO = "archivo.txt"
productos = [] 

## recargar la lista de diccionarios ##
print("6. Guardando productos actualizados (Sobrescribiendo archivo):")
print("Cargando datos existentes...")

try:
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            partes = linea_limpia.split(",")
            
            if len(partes) == 3:
                try:
                    nombre = partes[0].strip()
                    ## convertimos precio y cantidad para trabajar con ellos ##
                    precio = float(partes[1].strip().replace('.', '')) 
                    cantidad = int(partes[2].strip())
                    
                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except ValueError:
                    continue # Saltar a la siguiente línea si hay un error de conversion ##

except FileNotFoundError:
    print(f"[error] El archivo '{NOMBRE_ARCHIVO}' no se encontro No hay nada que guardar.")
    exit()

## Si quisiera modificar algo lo hacemos desde aca ##
for p in productos:
    if p["nombre"].lower() == "moto":
        p["cantidad"] += 10 # Se aumenta la cantidad de motos en 10
        print(f" Se simula la actualización: La cantidad de {p['nombre']} es ahora {p['cantidad']}.")
## sobreescribir el archivo con los datos de la lista ##
print("\nSobrescribiendo el archivo con la lista 'productos'...")

try:
    ## El modo 'w' sobreescribe todo el contenido anterior ##
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for producto in productos:
            linea_a_escribir = (
                f"{producto['nombre']},"
                f"{int(producto['precio'])}," 
                f"{producto['cantidad']}\n"
            )
            archivo.write(linea_a_escribir)
            
    print(f"\n Archivo '{NOMBRE_ARCHIVO}' sobrescrito exitosamente con {len(productos)} productos.")

except Exception as e:
    print(f"\n[error] No se pudo escribir en el archivo: {e}")


## comprobación final ##
print("\n nuevo contenido del archivo")
try:
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        contenido_completo = archivo.read()
        print(contenido_completo.strip())
except:
    pass
print("fin del programa :)\n")