
# %%
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np


# %% [markdown]
# ###  **Variables de entrada (Antecedentes)**
# #### Severidad del ataque (SA)
# #### Vulnerabilidad del sistema (VS)
# #### Exposicion al ataque (EA)
# #### Capacidad de respuesta (CR)

# %%

SA = ctrl.Antecedent(np.arange(0,11,1), 'severidad ataque')
VS = ctrl.Antecedent(np.arange(0,11,1), 'vulnerabilidad sistema')
EA = ctrl.Antecedent(np.arange(0,11,1), 'Exposición ataque')
CR = ctrl.Antecedent(np.arange(0,11,1), 'Capacidad respuesta')

# %% [markdown]
# ### **Variables de salida (Consecuentes)**
# 
# #### Nivel de riesgo (NR)

# %%
NR = ctrl.Consequent(np.arange(0,11,1),'Nivel riesgo')

# %% [markdown]
# ### **Conjuntos difusos**

# %%
SA['Sin impacto'] = fuzz.trapmf(SA.universe, [0,0,1,2])
SA['Minimo'] = fuzz.trimf(SA.universe, [1,2,3])
SA['Bajo'] = fuzz.trapmf(SA.universe, [2,3,4,5])
SA['Moderado'] = fuzz.trimf(SA.universe, [4,5,6])
SA['Alto'] = fuzz.trapmf(SA.universe, [5,6,7,8])
SA['Critico'] = fuzz.trapmf(SA.universe, [7,8,10,10])

# %%
SA.view()

# %%
VS['baja'] = fuzz.trapmf(VS.universe, [0,0,1,2])
VS['media baja'] = fuzz.trapmf(VS.universe, [1,2,3,4])
VS['media'] = fuzz.trapmf(VS.universe, [3,4,5,7])
VS['alta'] = fuzz.trapmf(VS.universe, [5,7,10,10])

# %%
VS.view()

# %%
EA['Minima'] = fuzz.trapmf(EA.universe, [0,0,2,3])
EA['Baja'] = fuzz.trapmf(EA.universe, [2,3,5,6])
EA['Moderada'] = fuzz.trapmf(EA.universe, [5,6,7,8])
EA['Alta'] = fuzz.trapmf(EA.universe,[7,8,10,10])

# %%
EA.view()

# %%
CR['Muy limitada'] = fuzz.trimf(CR.universe,[0,0,1])
CR['Basica'] = fuzz.trapmf(CR.universe, [0,1,3,4])
CR['Adecuada'] = fuzz.trapmf(CR.universe, [3,4,7,8])
CR['Avanzada'] = fuzz.trapmf(CR.universe, [6,8,10,10])

# %%
CR.view()

# %%
NR['Muy bajo'] = fuzz.trimf(NR.universe, [0,0,1])
NR['Bajo'] = fuzz.trapmf(NR.universe, [0,1,3,4])
NR['Moderado'] = fuzz.trapmf(NR.universe, [3,4,5,6])
NR['Alto'] = fuzz.trimf(NR.universe, [5,6,8])
NR['Critico'] = fuzz.trapmf(NR.universe, [6,8,10,10])

# %%
NR.view()

# %% [markdown]
# ## Crear reglas

# %%
regla1 = ctrl.Rule(SA['Sin impacto'] & VS['baja'], NR['muy_bajo'])
regla2 = ctrl.Rule(SA['bajo'] & VS['media_baja'], NR['bajo'])
regla3 = ctrl.Rule(SA['moderado'] & VS['media'], NR['moderado'])
regla4 = ctrl.Rule(SA['alto'] & VS['alta'], NR['alto'])
regla5 = ctrl.Rule(SA['muy_alto'] & VS['alta'], NR['critico'])

# La capacidad de respuesta seguirá influyendo en la mitigación del nivel de riesgo, por lo que debemos incluirla en las reglas
regla6 = ctrl.Rule(VS['alta'] & CR['basica'], NR['alto'])
regla7 = ctrl.Rule(VS['media'] & CR['adecuada'], NR['moderado'])
regla8 = ctrl.Rule(VS['baja'] & CR['avanzada'], NR['bajo'])

# %%
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
FIS = ctrl.ControlSystemSimulation(tipping_ctrl)

# %%
FIS.input['servicio'] = 2
FIS.input['comida'] = 5
FIS.compute()
print(FIS.output['propina'])
propina.view(sim=FIS)


