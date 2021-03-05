print("Calculadora con una sola variable \n")

print("**********************")
print("*  Menu de opciones **")
print("********************** \n")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto \n")

opcion = int(input("Introduce la opcion deseada: \n"))

if opcion == 1:
    print("Elegiste Suma \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", opcion)

elif opcion == 2:
    print("Elegiste Resta \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es: ", opcion)

elif opcion == 3:
   
    print("Elegiste la Multiplicacion \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion *= int(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicacion es: ", opcion)

elif opcion == 4:
    
    print("Elegiste Division \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion /= int(input("Introduce el segundo numero: "))
    print("El resultado de la Division es: ", opcion)

elif opcion == 5:
  
    print("Elegiste Division entera \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion //= int(input("Introduce el segundo numero: "))
    print("El resultado de la Division entera es: ", opcion)

elif opcion == 6:
    
    print("Elegiste Exponente \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion **= int(input("Introduce el segundo numero: "))
    print("El resultado del exponente es: ", opcion)

elif opcion == 7:
    
    print("Elegiste el Resto \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion %= int(input("Introduce el segundo numero: "))
    print("El resultado del resto es: ", opcion)

else:
    print(" Esta opcion no existe ")
    










