# Clase base: representa una transaccion (un movimiento de dinero)
# De esta clase heredan Ingreso y Egreso (relacion "es un")
class Transaccion:

    def __init__(self, monto, descripcion, categoria):
        self._monto = monto              # atributo "privado" (con guion bajo)
        self.descripcion = descripcion
        self.categoria = categoria

    # Getter y setter del monto (encapsulamiento)
    def get_monto(self):
        return self._monto

    def set_monto(self, nuevo_monto):
        if nuevo_monto < 0:
            print("El monto no puede ser negativo.")
        else:
            self._monto = nuevo_monto

    # Cada tipo de transaccion redefine como impacta en el saldo
    def impacto(self):
        return 0

    def mostrar(self):
        print(self.descripcion, "-", self.categoria, "- $", self._monto)


# Un Ingreso suma dinero
class Ingreso(Transaccion):

    def impacto(self):
        return self._monto

    def mostrar(self):
        print("INGRESO -", self.descripcion, "-", self.categoria, "- $", self._monto)


# Un Egreso resta dinero
class Egreso(Transaccion):

    def impacto(self):
        return -self._monto

    def mostrar(self):
        print("EGRESO  -", self.descripcion, "-", self.categoria, "- $", self._monto)
