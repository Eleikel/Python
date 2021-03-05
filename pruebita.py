class Gente():

    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
       
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar de Residencia: ", self.residencia)

    
    
class Trabajador(Gente):

    def __init__(self, salario, antiguedad, nombre_empleado, lugar_residencia):

        super().__init__(nombre_empleado, lugar_residencia)

        self.salario= salario
        self.antiguedad= antiguedad

    def descripcion(self):

        super().descripcion()

        print("Salario: ",self.salario, "\nTiempo de trabajo:", self.antiguedad)



Maria = Gente("KEKE", 2, "LA")
Maria.descripcion()