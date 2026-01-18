"""
Programa principal: Calculadora de Áreas
----------------------------------------
Este programa permite calcular el área de figuras geométricas (por ahora rectángulos).
Demuestra el uso de:
- Tipos de datos (int, float, str, bool)
- Identificadores en snake_case
- Estructura modular
- Comentarios explicativos
"""

from MODELOS.rectangulo import Rectangulo
from SERVICIOS.calculadora_servicio import CalculadoraServicio

def main():
    print("🔷 Bienvenido a la Calculadora de Áreas 🔷\n")

    # Crear instancia del servicio
    calculadora = CalculadoraServicio()

    # Pedir datos al usuario
    continuar = True
    while continuar:
        try:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))

            rect = Rectangulo(base, altura)
            calculadora.agregar_figura(rect)

            respuesta = input("¿Desea calcular otra figura? (s/n): ").strip().lower()
            continuar = respuesta == "s"

        except ValueError:
            print(" Error: Por favor ingrese valores numéricos válidos.")

    # Mostrar resultados
    calculadora.mostrar_resultados()
    print("\n Cálculo finalizado.")

if __name__ == "__main__":
    main()
