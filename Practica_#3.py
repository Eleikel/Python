print("*****************************************************")
print("* Programa para determinar ¿Cual es el numero mas grande de tres numeros? *")
print("*****************************************************")

primero = int(input("Introduce el primer numero: "))
segundo = int(input("Introduce el segundo numero: "))
tercero = int(input("Introduce el tercer numero: "))

if primero > segundo and primero > tercero:
    print("El numero mas grande es: ", primero)
elif segundo > tercero:
    print("El numero mas grande es: ", segundo)
else:
    print("El numero mas grande es: ", tercero)