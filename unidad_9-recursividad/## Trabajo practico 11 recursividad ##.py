## Trabajo practico 11 recursividad ##

## 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa ##
## función para calcular y mostrar en pantalla el factorial de todos los números enteros  ##
##entre 1 y el número que indique el usuario ##
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

## 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición ## 
## indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario  ##
## especifique ## 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un  ##
## exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un  ##
## algoritmo general.##
def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp-1)

## 4)  Crear una función recursiva en Python que reciba un número entero positivo en base  ##
## decimal y devuelva su representación en binario como una cadena de texto.##
def a_binario(n):
    if n == 0:
        return ""
    else:
        return a_binario(n//2) + str(n%2)

## 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una ##
## cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no  ##
##  lo es. ##
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

## 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un ##
## número entero positivo y devuelva la suma de todos sus dígitos. ##
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

## 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n ##
## bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al ##
## último nivel con un solo bloque ##
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n-1)

## 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un ##
## número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces ##
## aparece ese dígito dentro del número ##
def contar_digito(num, dig):
    if num == 0:
        return 0
    ultimo = num % 10
    if ultimo == dig:
        return 1 + contar_digito(num//10, dig)
    else:
        return contar_digito(num//10, dig)

## Programa principal ##
def main():
    print("Trabajo Practico 11 recursividad")
    
    while True:
        print("\nOpciones:")
        print("1. Calcular factorial")
        print("2. Serie Fibonacci") 
        print("3. Calcular potencia")
        print("4. Decimal a binario")
        print("5. Verificar palíndromo")
        print("6. Sumar digitos")
        print("7. Bloques de piramide")
        print("8. Contar digitos")
        print("9. Ver todos los ejercicios")
        print("0. Salir")
        
        opcion = input("\nEligi una opcion: ")
        
        if opcion == "1":
            num = int(input("Numero para factorial: "))
            if num < 0:
                print("El numero debe ser positivo")
            else:
                print(f"Factorial de {num} = {factorial(num)}")
                
        elif opcion == "2":
            pos = int(input("Posicion en Fibonacci: "))
            if pos < 0:
                print("La posicion debe ser positiva")
            else:
                print(f"Fibonacci en posición {pos} = {fibonacci(pos)}")
                print("Serie completa:", [fibonacci(i) for i in range(pos+1)])
                
        elif opcion == "3":
            base = float(input("Base: "))
            exp = int(input("Exponente: "))
            print(f"{base}^{exp} = {potencia(base, exp)}")
            
        elif opcion == "4":
            num = int(input("Numero decimal: "))
            binario = a_binario(num)
            if binario == "":
                binario = "0"
            print(f"{num} en binario = {binario}")
            
        elif opcion == "5":
            palabra = input("Palabra: ").lower()
            if es_palindromo(palabra):
                print(f"'{palabra}' es palindromo")
            else:
                print(f"'{palabra}' no es palindromo")
                
        elif opcion == "6":
            num = int(input("Numero: "))
            print(f"Suma de dígitos de {num} = {suma_digitos(num)}")
            
        elif opcion == "7":
            base = int(input("Bloques en base: "))
            print(f"Total de bloques: {contar_bloques(base)}")
            
        elif opcion == "8":
            num = int(input("Numero: "))
            dig = int(input("Digito a contar: "))
            print(f"El digito {dig} aparece {contar_digito(num, dig)} veces")
            
        elif opcion == "9":
            print("\n ejemplos de los ejercicios")
            
            ## Factorial ##
            print(f"\n1. Factorial de 5 = {factorial(5)}")
            
            ## Fibonacci ## 
            fib_6 = [fibonacci(i) for i in range(6)]
            print(f"2. Fibonacci hasta posicion 5: {fib_6}")
            
            ## Potencia ##
            print(f"3. 2^4 = {potencia(2, 4)}")
            
            ## Binario ##
            print(f"4. 10 en binario = {a_binario(10)}")
            
            ## Palindromo ##
            print(f"5. 'reconocer' es palindromo: {es_palindromo('reconocer')}")
            
            ## Suma dígitos ##
            print(f"6. Suma digitos de 123 = {suma_digitos(123)}")
            
            ## Bloques ##
            print(f"7. Bloques para base 4 = {contar_bloques(4)}")
            
            ## Contar dígios ##
            print(f"8. Digito 2 en 1223 = {contar_digito(1223, 2)}")
            
        elif opcion == "0":
            print("¡adios!")
            break
            
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()