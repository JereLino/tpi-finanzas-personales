from decoradores import registrar_carga


# El GestorFinanzas es el "dueño del proceso".
# Guarda las transacciones (composicion) y pide los reportes.
class GestorFinanzas:

    def __init__(self):
        self.transacciones = []          # composicion: contiene transacciones

    # El decorador @registrar_carga le agrega los mensajes
    # de "registrando..." y "registrada con exito" sin tocar este metodo.
    @registrar_carga
    def agregar(self, transaccion):
        self.transacciones.append(transaccion)

    def listar(self):
        if len(self.transacciones) == 0:
            print("No hay transacciones cargadas.")
        else:
            for t in self.transacciones:
                t.mostrar()

    # Aca se usa el patron Strategy:
    # el gestor NO sabe como se arma el reporte,
    # solo le pide a la estrategia que lo genere.
    def generar_reporte(self, estrategia):
        estrategia.generar(self.transacciones)
