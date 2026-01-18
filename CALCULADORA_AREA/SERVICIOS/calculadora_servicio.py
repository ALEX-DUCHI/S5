"""
Módulo: calculadora_servicio.py
Contiene la clase CalculadoraServicio que gestiona las operaciones de cálculo.
"""

class CalculadoraServicio:
    def __init__(self):
        self.figuras = []  # Lista de figuras geométricas

    def agregar_figura(self, figura):
        """Agrega una figura a la lista."""
        self.figuras.append(figura)

    def mostrar_resultados(self):
        """Muestra la información de todas las figuras registradas."""
        print("\n📐 Resultados de Cálculo de Áreas:\n")
        for figura in self.figuras:
            print(f"{figura.mostrar_informacion()} → Área: {figura.calcular_area()} unidades²")
