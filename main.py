"""
Programme fait par Raul Mic Nicolas
TP4 : Introduction à la programmation OO
Écrire une classe Cercle qui aura
  a) deux méthodes: calcul_aire et calcul_circonference. Les deux méthodes retournent le résultat du calcul.
  b) un attribut pour conserver la valeur du rayon.

"""

from math import pi


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_aire(self):
        return pi * self.rayon * self.rayon

    def calculer_circonference(self):
        return 2 * pi * self.rayon


cercle = Cercle(520)
print(f"L'aire d'un circle avec le rayon {cercle.rayon} est égale à {cercle.calculer_aire()}")
print(f"La circonference d'un circle avec le rayon {cercle.rayon} est égale à {cercle.calculer_circonference()}")
