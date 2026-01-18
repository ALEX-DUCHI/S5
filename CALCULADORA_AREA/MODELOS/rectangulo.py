"""
Módulo: rectangulo.py
Define una subclase de Figura: Rectángulo.
Usa atributos float y demuestra herencia, encapsulación y polimorfismo.
"""

from MODELOS.figura import Figura

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura
        self.es_valido = base > 0 and altura > 0  # Tipo booleano

    def calcular_area(self) -> float:
        """Devuelve el área del rectángulo si las dimensiones son válidas."""
        if self.es_valido:
            return self.base * self.altura
        else:
            print("❌ Error: Las medidas deben ser positivas.")
            return 0.0

    def mostrar_informacion(self):
        """Devuelve una cadena con la información detallada."""
        return f"{super().mostrar_informacion()} | Base: {self.base} | Altura: {self.altura}"
