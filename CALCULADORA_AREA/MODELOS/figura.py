"""
Módulo: figura.py
Define la clase base abstracta Figura, que representa una figura geométrica.
Usa abstracción y polimorfismo (cada subclase implementa su propio cálculo de área).
"""

from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre  # Tipo string

    @abstractmethod
    def calcular_area(self) -> float:
        """Método abstracto: calcular el área de la figura."""
        pass

    def mostrar_informacion(self):
        """Devuelve el nombre de la figura."""
        return f"Figura: {self.nombre}"
