

codigo = int(input("Introduzca el codigo en el Articulo: "))
print(codigo)

nombre = (input("Introduzca el Nombre en el Articulo: "))
print(nombre)

cantidad = (input("Introduzca la Cantidad comprada: "))
cantidad = int(cantidad)
print(cantidad)

precio = (input("Introduzca el precio en el Articulo: "))
precio = int(cantidad)
print(precio)

stotal = cantidad * precio
stotal =float(stotal)
itb = stotal * 0.16
itb = float(itb)
stotal = stotal + itb
stotal = float(stotal)
desc = stotal * 0.05
desc = float(desc)
total = stotal - desc
total = float(total)


print("CODIGO DEL PRODUCTO: ",codigo)
print("NOMBRE DEL PRODUCTO: ", nombre)
print("PRECIO DEL PRODUCTO: ", precio)
print("CANTIDAD COMPRADA: ", cantidad)
print("TOTAL POR LA COMPRA: ", cantidad ** precio)
print("ITEBIS: ", itb)
print("SUBTOTAL A PAGAR : ", stotal)
print("DESCUENTO : ", desc)
print("TOTAL FINAL :", total)


