#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:26:37 2024

@author: miguel
"""

from pyds import MassFunction

# Funciones de masa de creencia para perros y gatos
m_perro = MassFunction({'perro': 0.7, 'gato': 0.3})
m_gato = MassFunction({'perro': 0.2, 'gato': 0.8})

# Combinación de las funciones de masa de creencia
m_combined = m_perro.combine_conjunctive(m_gato)

# Tomar una decisión basada en la creencia combinada
if m_combined.bel({'perro'}) > m_combined.bel({'gato'}):
    print("El clasificador predice que es un perro.")
else:
    print("El clasificador predice que es un gato.")
"""************************************"""
from pyds import MassFunction

# Observaciones de características de perros y gatos (con incertidumbre)
observaciones_perro = {'orejas_grandes': 0.7, 'pelaje_marron': 0.8, 'cola_larga': 0.6}
observaciones_gato = {'orejas_puntiagudas': 0.9, 'pelaje_rayas': 0.85, 'cola_corta': 0.7}

# Funciones de masa de creencia para perros y gatos
m_perro = MassFunction(observaciones_perro)
m_gato = MassFunction(observaciones_gato)

# Combinación de las funciones de masa de creencia
m_combined = m_perro.combine_conjunctive(m_gato)

# Tomar una decisión basada en la creencia combinada
if m_combined.bel({'perro'}) > m_combined.bel({'gato'}):
    print("El clasificador predice que es un perro.")
else:
    print("El clasificador predice que es un gato.")
