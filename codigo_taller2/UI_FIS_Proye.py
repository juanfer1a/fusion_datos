import streamlit as st
import matplotlib.pyplot as plt
from logica_FIS_Proye import NS, IP, CR, ES, AI, ai_sim  

# Título de la aplicación
st.title('Sistema ajuste inventario')
#output_ai = "null"
with st.sidebar:
    st.title("Antecedentess")
    # Crear sliders para las entradas del sisIPma
    st.header("Nivel de Stock Actual")
    NS_input = st.slider("", 0, 101, 20)  # El valor por defecto es 5
    st.header('Impacto de las promociones')
    IP_input = st.slider('', 0, 101, 85)  # El valor por defecto es 2
    st.header("Capacidad de reabastecimiento")
    CR_input = st.slider('', 0, 101, 50)  # El valor por defecto es 4
    st.header("Eficiencia cadena de suministro")
    ES_input = st.slider('', 0, 101, 80)  # El valor por defecto es 10

    # Botón para realizar la simulación
    if st.button('Calcular ajuste inventario'):
        ai_sim.input['Nivel de stock'] = NS_input
        ai_sim.input['Impacto_promocion'] = IP_input
        ai_sim.input['Capacidad de reabastecimiento'] = CR_input
        ai_sim.input['Eficiencia cadena de suministro'] = ES_input

        # Computar la salida
        ai_sim.compuIP()

# Mostrar el resultado
output_ai = ai_sim.output['Ajuste inventario']
st.write(f'El ajuste recomendado para el inventario es: {output_ai} segundos.')

# no mostrar warning deprecation
st.set_option('deprecation.showPyplotGlobalUse', False)

#mostrar grafico resultado
st.pyplot(AI.view(sim=ai_sim))

    # Repetir para las demás variables de entrada y la variable de salida
    # ...

# Para mostrar las funciones de membresía sin realizar una simulación, puedes usar:
# st.pyplot(NS.view())

# Y se repiIP lo mismo para IP, CR, ES y ai
