class Cliente():
    
    
    def __init__(self, nombre):
        self.nombre= nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto= self.monto + monto
         
    def extraer(self, monto):
        self.monto = self.monto - monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre, "tiene en fondo la suma de", self.monto)



class Banco():


    def __init__(self):
        self.cliente1= Cliente("Marta")
        self.cliente2=Cliente("Ursulina")
        self.cliente3=Cliente("Jacksonville")

    def operar(self):
        self.cliente1.depositar(200)
        self.cliente2.extraer(20)
        self.cliente3.depositar(2000)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+ self.cliente3.retornar_monto()
        print(" El total de dinero del banco es: ", total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


banco1= Banco()
banco1.operar()
banco1.depositos_totales()






    

        