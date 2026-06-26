from decoradores import registrar_carga


# Clase principal para manejar los movimientos
class GestorFinanzas:

    def __init__(self):
        self.transacciones = []          # composicion: contiene transacciones

# Agrega una transacción y avisa por consola gracias al decorador
    @registrar_carga
    def agregar(self, transaccion):
        self.transacciones.append(transaccion)

    def listar(self):
        if len(self.transacciones) == 0:
            print("No hay transacciones cargadas.")
        else:
            for t in self.transacciones:
                t.mostrar()

# Ejecuta el reporte según la opción que le pases
        estrategia.generar(self.transacciones)
