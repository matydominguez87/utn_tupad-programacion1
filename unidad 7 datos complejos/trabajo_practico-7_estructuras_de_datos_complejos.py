## diccionario precios de frutas ##

## 1 ejercicio de añadir frutas ##

precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

## Añadir nuevas frutas ##
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario despues de añadir frutas:")
print(precios_frutas)

## 2 actualizar precios ##
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nDiccionario después de actualizar precios:")
print(precios_frutas)

## 3 crear lista solo frutas ##

lista_frutas = list(precios_frutas.keys())

print("\nLista de frutas (solo claves):")
print(lista_frutas)

## 4 programa de numeros telefonicos ##
def programa_telefonos():
    agenda = {}
    NUM_CONTACTOS = 5

    ##  Cargar 5 contactos ##
    print(f" Carga de {NUM_CONTACTOS} contactos ")
    for i in range(NUM_CONTACTOS):
        ## Solicitud y validacion simple de nombre ##
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ").strip()
        ## Solicitud y validación simple de numero ##
        numero = input(f"Ingrese el número telefonico de {nombre}: ").strip()

        ## Almacenar en el diccionario ##
        agenda[nombre] = numero
    
    print("\n Carga de contactos finalizada ")
    print("Agenda actual:", agenda)

    ## Consultar un numero ##
    print("\n Consulta de numero telefonico ")
    nombre_consulta = input("Ingrese el nombre del contacto q desea consultar: ").strip()

    ## Verificar si el nombre existe en las claves del diccionario ##
    if nombre_consulta in agenda:
        ## Si existe, mostrar el número asociado ##
        numero_asociado = agenda[nombre_consulta]
        print(f"El numero de telefono de {nombre_consulta} es: {numero_asociado}")
    else:
        ## Si no existe mostrar un mensaje de error ##
        print(f" error el contacto '{nombre_consulta}' no se encontro en la agenda.")


programa_telefonos()


## 5  Solicitar la frase al usuario ##
frase = input("ingresa una frase: ")
palabras = frase.lower().split()
## Imprimir las palabras unicas ##
palabras_unicas = set(palabras)
print("las palabras unicas:")
print(palabras_unicas)

##diccionario con la frecuencia de cada palabra ##
frecuencia_palabras = {}
for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1


print(" diccionario con la cantidad de veces que aparece cada palabra:")
print(frecuencia_palabras)
## 6 alumnos ##

def calcular_promedios_alumnos():
    ## diccionario para almacenar los datos ##
    registro_alumnos = {}
    NUM_ALUMNOS = 3
    NUM_NOTAS = 3

    print(" ingreso de Notas de Alumnos ")
    
    ## Bucle para ingresar los datos de los 3 alumnos ##
    for i in range(NUM_ALUMNOS):
        nombre = input(f"\n ingrese el nombre del alumno {i + 1}: ").strip()
        
        ## Lista temporal para las notas antes de convertirlas a tupla ##
        notas_lista = []
        
        ## Bucle para ingresar las 3 notas para el alumno actual ##
        for j in range(NUM_NOTAS):
            ## bucle while para asegurar la entrada sea un valida ##
            while True:
                try:
                    nota = float(input(f"  Ingrese la nota {j + 1} de {nombre}: "))
                    notas_lista.append(nota)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        
        ##  lista de notas a tupla y almacenarla en el diccionario ##
        registro_alumnos[nombre] = tuple(notas_lista)

    print("\n resultados de promedios ")
    
    ## Bucle para calcular y mostrar el promedio de cada alumno ##
    for nombre, notas in registro_alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} (Notas: {notas}) es: {promedio:.2f}")

calcular_promedios_alumnos()

## 7  Dados los dos sets de estudiantes que aprobaron Parcial 1 y Parcial 2 ##
aprobados_p1 = {10, 15, 18, 25 , 4 , 12 }
aprobados_p2 = {15, 12, 23 , 30 , 12 , 8 }

print(" ANALISIS DE RESULTADOS DE PARCIALES ")
print(f"Aprobaron P1: {aprobados_p1}")
print(f"Aprobaron P2: {aprobados_p2}")

## los que aprobaron ambos parciales (Interseccion) ##
aprobados_ambos = aprobados_p1 & aprobados_p2

print("\n  estudiantes que aprobaron ambos parciales :")
print(aprobados_ambos)

## Mostra los que aprobaron solo uno de los dos (Diferencia Simetrica) ##
aprobados_solo_uno = aprobados_p1 ^ aprobados_p2

print("\n estudiantes que aprobaron solo uno de los dos:")
print(aprobados_solo_uno)

## total de estudiantes que aprobaron al menos un parcial (Union) ##
aprobados_total = aprobados_p1 | aprobados_p2

print("\n lista total de estudiantes que aprobaron al menos un parcial")
print(aprobados_total)

def gestionar_stock():
    ##8  Diccionario inicial de stock ## 
    stock_productos = {
        'ruedas': 50,
        'frenos': 100,
        'manubrios': 30,
        'pedales': 80
    }

    print(" gestion de stock de productos ")
    print(f"stock inicial: {stock_productos}")

    while True:
        nombre_producto = input("\n ingrese el nombre del producto 'salir' para terminar): ").lower().strip()

        if nombre_producto == 'salir':
            print("\n gestion de stock finalizada")
            print(f"stock final: {stock_productos}")
            break

        ## consultar el stock /  agregar unidades / agregar nuevo producto ##
        
        if nombre_producto in stock_productos:
            ## Producto existente (Consulta y Agrega unidades) ##
            stock_actual = stock_productos[nombre_producto]
            print(f"Stock actual de '{nombre_producto}': {stock_actual} unidades.")

            try:
                unidades_a_agregar = int(input(f"cuantas unidades desea agregar a '{nombre_producto}'? (Ingrese 0 si solo queria consultar): "))
                if unidades_a_agregar >= 0:
                    stock_productos[nombre_producto] += unidades_a_agregar
                    print(f"Stock actualizado. Nuevo stock de '{nombre_producto}': {stock_productos[nombre_producto]}")
                else:
                    print(" ingrese un numero positivo o cero.")
            except ValueError:
                print(" error: Ingrese un numero entero valido.")
        else:
            ### producto no existe (Agregar nuevo producto) ##
            print(f"el producto '{nombre_producto}' no existe en el stock.")
            
            ## Preguntar si quiere agregarlo ##
            respuesta = input("queres agregar este nuevo producto? (si/no): ").lower().strip()
            
            if respuesta == 'si':
                while True:
                    try:
                        stock_inicial = int(input(f"Ingrese el stock inicial para '{nombre_producto}': "))
                        if stock_inicial >= 0:
                            stock_productos[nombre_producto] = stock_inicial
                            print(f"producto '{nombre_producto}' agregado con stock inicial de {stock_inicial}!")
                            break
                        else:
                            print("el stock inicial no puede ser negativo.")
                    except ValueError:
                        print("Error: Ingrese un numero entero valido.")
            else:
                print("Producto no agregado.")

gestionar_stock()

## 9 agenda ##
agenda = {
    ("lunes", 9): "Reunion de equipo",
    ("lunes", 14): "Preparar luchas",
    ("martes", 10): "Llamada con sponsors",
    ("miércoles", 16): "Clase de jiu-jitsu",
    ("jueves", 11): "mantenimiento al auto",
    ("viernes", 15): "turno con el dentista",
    ("sábado", 18): "futbol con amigos "
}

def consultar_evento(dia, hora):
    clave = (dia.lower(), hora) ## Aseguramos que el día este en minusculas para la busqueda ##

    if clave in agenda:
        return f"el evento para el {dia.capitalize()} a las {hora:02d}:00 es: **{agenda[clave]}**"
    else:
        return f"No hay eventos programados para el {dia.capitalize()} a las {hora:02d}:00."
    
def mostrar_toda_la_agenda():
    print("\n agenda semanal ")
    ## Recorrer y ordenar los eventos para mostrarlos de forma clara ##
    eventos_ordenados = sorted(agenda.items())
    
    for (dia, hora), evento in eventos_ordenados:
        print(f"[{dia.capitalize():<10} @ {hora:02d}:00] -> {evento}")
    
    print("-" * 28)

if __name__ == "__main__":
    mostrar_toda_la_agenda()    



## 10  diccionario ##

## Diccionario original ##
paises_capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma",
    "Argentina": "Buenos Aires"
}

## Nuevo diccionario ##
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print(f"Diccionario Original: {paises_capitales}")
print(f"Nuevo Diccionario (Invertido): {capitales_paises}")