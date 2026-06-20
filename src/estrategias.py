# PATRON STRATEGY
# Cada estrategia sabe generar un reporte distinto.
# El gestor puede cambiar de estrategia sin cambiar su codigo.

# Estrategia base: todas las estrategias tienen el metodo generar()
class EstrategiaReporte:

    def generar(self, transacciones):
        pass


# Reporte 1: muestra solo el saldo actual
class ReporteBalance(EstrategiaReporte):

    def generar(self, transacciones):
        total = 0
        for t in transacciones:
            total = total + t.impacto()
        print("=== BALANCE GENERAL ===")
        print("Saldo actual: $", total)


# Reporte 2: muestra total de ingresos, total de egresos y saldo
class ReporteResumen(EstrategiaReporte):

    def generar(self, transacciones):
        total_ingresos = 0
        total_egresos = 0
        for t in transacciones:
            valor = t.impacto()
            if valor > 0:
                total_ingresos = total_ingresos + valor
            else:
                total_egresos = total_egresos + (-valor)   # lo paso a positivo
        print("=== RESUMEN ===")
        print("Total ingresos: $", total_ingresos)
        print("Total egresos:  $", total_egresos)
        print("Saldo:          $", total_ingresos - total_egresos)


# Reporte 3: agrupa los montos por categoria
class ReportePorCategoria(EstrategiaReporte):

    def generar(self, transacciones):
        print("=== POR CATEGORIA ===")
        categorias = {}
        for t in transacciones:
            if t.categoria in categorias:
                categorias[t.categoria] = categorias[t.categoria] + t.impacto()
            else:
                categorias[t.categoria] = t.impacto()
        for nombre in categorias:
            print(nombre, ": $", categorias[nombre])
