# TPI - Gestor de Finanzas Personales

Trabajo Práctico Integrador - Programación Avanzada (UNAB) - 2026

## Integrantes
- Machado Nicolas Perez
- Ruiz Celeste
- Pascolo Jeremias

## Descripción
Aplicación de consola para llevar el control de las finanzas personales.
Permite cargar ingresos y egresos, ver el estado actual (balance) y generar
distintos reportes (resumen y por categoría).

## Diagrama de clases (UML)

```mermaid
classDiagram
    class Transaccion {
        -monto
        +descripcion
        +categoria
        +get_monto()
        +set_monto()
        +impacto()
        +mostrar()
    }
    class Ingreso {
        +impacto()
        +mostrar()
    }
    class Egreso {
        +impacto()
        +mostrar()
    }
    class GestorFinanzas {
        +transacciones
        +agregar()
        +listar()
        +generar_reporte()
    }
    class EstrategiaReporte {
        +generar()
    }
    class ReporteBalance {
        +generar()
    }
    class ReporteResumen {
        +generar()
    }
    class ReportePorCategoria {
        +generar()
    }

    Transaccion <|-- Ingreso
    Transaccion <|-- Egreso
    GestorFinanzas o-- Transaccion
    GestorFinanzas ..> EstrategiaReporte : usa (Strategy)
    EstrategiaReporte <|-- ReporteBalance
    EstrategiaReporte <|-- ReporteResumen
    EstrategiaReporte <|-- ReportePorCategoria
```

## Conceptos aplicados
- **Programación Orientada a Objetos**
  - Abstracción: la clase `Transaccion` define la base común.
  - Encapsulamiento: el monto es privado (`_monto`) y se accede con getter/setter.
  - Herencia: `Ingreso` y `Egreso` heredan de `Transaccion` (relación "es un").
  - Polimorfismo: cada transacción redefine `impacto()` (un ingreso suma, un egreso resta).
- **Relación entre objetos**
  - Composición: `GestorFinanzas` contiene una lista de `Transaccion`.
- **Patrón de diseño**
  - Strategy: los reportes (`ReporteBalance`, `ReporteResumen`, `ReportePorCategoria`)
    son estrategias intercambiables. El gestor no sabe cómo se arma el reporte,
    solo le pide a la estrategia que lo genere.
- **Decorador**
  - `registrar_carga`: agrega mensajes al cargar una transacción sin modificar
    el código del método `agregar` del gestor.

## Estructura del proyecto
```
tpi_finanzas/
├── README.md
└── src/
    ├── transacciones.py   (Transaccion, Ingreso, Egreso)
    ├── estrategias.py     (patrón Strategy: reportes)
    ├── decoradores.py     (decorador registrar_carga)
    ├── gestor.py          (GestorFinanzas)
    └── main.py            (menú de consola)
```

## Cómo ejecutar
1. Tener Python 3 instalado.
2. Abrir una terminal dentro de la carpeta `src`.
3. Ejecutar:
```
python main.py
```
4. Usar el menú para cargar ingresos/egresos y ver los reportes.

## Modo de uso
Al iniciar se muestra un menú. Se escribe el número de la opción y Enter:

- **1 - Cargar ingreso** / **2 - Cargar egreso**: pide descripción, categoría y monto
  (el monto se escribe sin símbolo `$` ni puntos, por ejemplo `50000`).
- **3 - Ver todas las transacciones**: lista lo cargado.
- **4 - Ver balance**: muestra el saldo actual (ingresos menos egresos).
- **5 - Ver reportes**: abre un submenú donde se elige una letra:
  - `a` → Resumen (total ingresos, total egresos y saldo).
  - `b` → Por categoría (cuánto suma cada categoría).
- **6 - Salir**: cierra la aplicación.

Ejemplo de carga de un ingreso:
```
Descripcion: Sueldo
Categoria: Trabajo
Monto: 50000
Registrando nueva transaccion...
Transaccion registrada con exito!
```
