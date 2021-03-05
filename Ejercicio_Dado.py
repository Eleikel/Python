import random

dado1= random.randint(1,6)
dado2=random.randint(1, 6)
print("Primer dado: ", dado1)
print("Segundo dado: ", dado1)
dadoTotal= [dado1+dado2]

if dadoTotal==7:
    print("Ganaste")

else:
    print("Perdiste")