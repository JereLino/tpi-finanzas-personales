from transacciones import Ingreso, Egreso
from gestor import GestorFinanzas
from estrategias import ReporteBalance, ReporteResumen, ReportePorCategoria


def cargar_ingreso(gestor):
    descripcion = input("Descripcion: ")
    categoria = input("Categoria: ")
    monto = float(input("Monto: "))
    ingreso = Ingreso(monto, descripcion, categoria)
    gestor.agregar(ingreso)


def cargar_egreso(gestor):
    descripcion = input("Descripcion: ")
    categoria = input("Categoria: ")
    monto = float(input("Monto: "))
    egreso = Egreso(monto, descripcion, categoria)
    gestor.agregar(egreso)


def mostrar_menu():
    print("")
    print("===== FINANZAS PERSONALES =====")
    print("1. Cargar ingreso")
    print("2. Cargar egreso")
    print("3. Ver todas las transacciones")
    print("4. Ver balance")
    print("5. Ver reportes")
    print("6. Salir")


def main():
    gestor = GestorFinanzas()

    opcion = ""
    while opcion != "6":
        mostrar_menu()
        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            cargar_ingreso(gestor)
        elif opcion == "2":
            cargar_egreso(gestor)
        elif opcion == "3":
            gestor.listar()
        elif opcion == "4":
            gestor.generar_reporte(ReporteBalance())
        elif opcion == "5":
            print("a. Resumen (ingresos, egresos, saldo)")
            print("b. Por categoria")
            sub = input("Elegi un reporte: ")
            if sub == "a":
                gestor.generar_reporte(ReporteResumen())
            elif sub == "b":
                gestor.generar_reporte(ReportePorCategoria())
            else:
                print("Opcion invalida.")
        elif opcion == "6":
            print("Hasta luego!")
        else:
            print("Opcion invalida.")


main()
