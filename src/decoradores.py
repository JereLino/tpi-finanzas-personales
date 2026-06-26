# Decorador: agrega un mensaje antes y despues de cargar una transaccion
def registrar_carga(funcion):
    def funcion_nueva(self, transaccion):
        print("Registrando nueva transaccion...")
        funcion(self, transaccion)
        print("Transaccion registrada con exito!")
    return funcion_nueva
