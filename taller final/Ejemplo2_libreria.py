#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:51:48 2024

@author: miguel
pip install git+https://github.com/reineking/pyds.git

"""

import pyds as pyd

from itertools import product

#from pyds import MassFunction

# Crear una función de masa con hipótesis
m1 = pyd.MassFunction({'a': 0.1, 'b': 0.2, 'ab': 0.6, '': 0.1})

# Otra función de masa basada en evidencia diferente
m2 = pyd.MassFunction({'a': 0.3, 'ac': 0.4, 'c': 0.3})

# Combina las dos funciones de masa utilizando la regla de Dempster
combined_m = m1.combine_conjunctive(m2)

# Imprimir las funciones de masa combinadas
print("Función de masa combinada:", combined_m)

# Calcular la función de creencia
belief = combined_m.bel()

# Calcular la función de plausibilidad
plausibility = combined_m.pl()

# Imprimir funciones de creencia y plausibilidad
print("Función de creencia:", belief)
print("Función de plausibilidad:", plausibility)