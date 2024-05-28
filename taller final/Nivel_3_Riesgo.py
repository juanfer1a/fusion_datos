# %%
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd

# Definir las variables de entrada y salida difusas
creencia = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'creencia')
plausibilidad = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'plausibilidad')
probabilidad_pignistica = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'probabilidad_pignistica')

riesgo_discrepancia = ctrl.Consequent(np.arange(0, 11, 1), 'riesgo_discrepancia')
impacto_potencial = ctrl.Consequent(np.arange(0, 11, 1), 'impacto_potencial')
probabilidad_ocurrencia = ctrl.Consequent(np.arange(0, 11, 1), 'probabilidad_ocurrencia')

# Definir las funciones de membresía para cada variable
creencia.automf(3)
plausibilidad.automf(3)
probabilidad_pignistica.automf(3)

riesgo_discrepancia.automf(3)
impacto_potencial.automf(3)
probabilidad_ocurrencia.automf(3)

creencia.view()
plausibilidad.view()
probabilidad_pignistica.view()

riesgo_discrepancia.view()
impacto_potencial.view()
probabilidad_ocurrencia.view()


# Definir las reglas difusas
rule1 = ctrl.Rule(creencia['poor'] & plausibilidad['poor'] & probabilidad_pignistica['poor'], 
                  (riesgo_discrepancia['poor'], impacto_potencial['poor'], probabilidad_ocurrencia['poor']))
rule2 = ctrl.Rule(creencia['average'] & plausibilidad['average'] & probabilidad_pignistica['average'], 
                  (riesgo_discrepancia['average'], impacto_potencial['average'], probabilidad_ocurrencia['average']))
rule3 = ctrl.Rule(creencia['good'] & plausibilidad['good'] & probabilidad_pignistica['good'], 
                  (riesgo_discrepancia['good'], impacto_potencial['good'], probabilidad_ocurrencia['good']))

# Crear el sistema de control difuso
riesgo_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
riesgo = ctrl.ControlSystemSimulation(riesgo_ctrl)


# %%
# Cargar los resultados del Nivel 2
resultados_nivel2 = pd.read_csv('resultados_dempster_shafer.csv')

# Inicializar las listas para almacenar las salidas del FIS
riesgo_discrepancias = []
impactos_potenciales = []
probabilidades_ocurrencias = []

# Aplicar el FIS a cada conjunto de valoraciones del Nivel 2
for i in range(len(resultados_nivel2)):
    riesgo.input['creencia'] = resultados_nivel2['Creencia'][i]
    riesgo.input['plausibilidad'] = resultados_nivel2['Plausibilidad'][i]
    riesgo.input['probabilidad_pignistica'] = resultados_nivel2['Probabilidad_Pignistica'][i]
    
    # Calcular las salidas del FIS
    riesgo.compute()
    
    # Almacenar las salidas
    riesgo_discrepancias.append(riesgo.output['riesgo_discrepancia'])
    impactos_potenciales.append(riesgo.output['impacto_potencial'])
    probabilidades_ocurrencias.append(riesgo.output['probabilidad_ocurrencia'])

# Guardar las salidas en un archivo CSV
salidas_fis = pd.DataFrame({
    'Riesgo_Discrepancia': riesgo_discrepancias,
    'Impacto_Potencial': impactos_potenciales,
    'Probabilidad_Ocurrencia': probabilidades_ocurrencias
})
salidas_fis.to_csv('salidas_fis.csv', index=False)

print("Salidas del FIS guardadas en 'salidas_fis.csv'")


# %%
from pyds import MassFunction

# Cargar las salidas del FIS
salidas_fis = pd.read_csv('salidas_fis.csv')

# Definir las funciones de masa iniciales
mass_functions = []

for i in range(len(salidas_fis)):
    riesgo_discrepancia = salidas_fis['Riesgo_Discrepancia'][i]
    impacto_potencial = salidas_fis['Impacto_Potencial'][i]
    probabilidad_ocurrencia = salidas_fis['Probabilidad_Ocurrencia'][i]
    
    mass_function_riesgo = MassFunction({'bajo': 1.0}) if riesgo_discrepancia <= 3.33 else MassFunction({'medio': 1.0}) if riesgo_discrepancia <= 6.66 else MassFunction({'alto': 1.0})
    mass_function_impacto = MassFunction({'bajo': 1.0}) if impacto_potencial <= 3.33 else MassFunction({'medio': 1.0}) if impacto_potencial <= 6.66 else MassFunction({'alto': 1.0})
    mass_function_probabilidad = MassFunction({'bajo': 1.0}) if probabilidad_ocurrencia <= 3.33 else MassFunction({'medio': 1.0}) if probabilidad_ocurrencia <= 6.66 else MassFunction({'alto': 1.0})
    
    mass_functions.append((mass_function_riesgo, mass_function_impacto, mass_function_probabilidad))

# Combinar las funciones de masa utilizando la regla de combinación de Dempster para cada conjunto de salidas
riesgo_final = MassFunction()
impacto_final = MassFunction()
probabilidad_final = MassFunction()

for mass_function_riesgo, mass_function_impacto, mass_function_probabilidad in mass_functions:
    riesgo_final = riesgo_final & mass_function_riesgo if riesgo_final else mass_function_riesgo
    impacto_final = impacto_final & mass_function_impacto if impacto_final else mass_function_impacto
    probabilidad_final = probabilidad_final & mass_function_probabilidad if probabilidad_final else mass_function_probabilidad

# Obtener la creencia, plausibilidad y probabilidad pignística de la valoración final
creencia_riesgo = riesgo_final.bel({'bajo', 'medio', 'alto'})
plausibilidad_riesgo = riesgo_final.pl({'bajo', 'medio', 'alto'})
pignistic_riesgo = riesgo_final.pignistic()

creencia_impacto = impacto_final.bel({'bajo', 'medio', 'alto'})
plausibilidad_impacto = impacto_final.pl({'bajo', 'medio', 'alto'})
pignistic_impacto = impacto_final.pignistic()

creencia_probabilidad = probabilidad_final.bel({'bajo', 'medio', 'alto'})
plausibilidad_probabilidad = probabilidad_final.pl({'bajo', 'medio', 'alto'})
pignistic_probabilidad = probabilidad_final.pignistic()

# Guardar los resultados en un archivo CSV
resultados_nivel3 = pd.DataFrame({
    'Creencia_Riesgo': [creencia_riesgo],
    'Plausibilidad_Riesgo': [plausibilidad_riesgo],
    'Probabilidad_Pignistica_Riesgo': [pignistic_riesgo],
    'Creencia_Impacto': [creencia_impacto],
    'Plausibilidad_Impacto': [plausibilidad_impacto],
    'Probabilidad_Pignistica_Impacto': [pignistic_impacto],
    'Creencia_Probabilidad': [creencia_probabilidad],
    'Plausibilidad_Probabilidad': [plausibilidad_probabilidad],
    'Probabilidad_Pignistica_Probabilidad': [pignistic_probabilidad]
})
resultados_nivel3.to_csv('resultados_nivel3.csv', index=False)

print("Resultados del Nivel 3 guardados en 'resultados_nivel3.csv'")



