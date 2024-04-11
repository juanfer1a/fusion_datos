import streamlit as st
import matplotlib.pyplot as plt
from logica_FIS_gestion_trafico import QV, TE, HD, CM, TS, ts_sim  

# Título de la aplicación
st.title('Sistema de Control de Semáforo')
#output_ts = "null"
with st.sidebar:
    st.title("Antecedentes")
    # Crear sliders para las entradas del sistema
    st.header("Cantidad de vehiculos")
    qv_input = st.slider("", 0, 10, 5)  # El valor por defecto es 5
    st.header('Tiempo de Espera')
    te_input = st.slider('', 0, 10, 2)  # El valor por defecto es 2
    st.header("Hora del Día")
    hd_input = st.slider('', 0, 10, 4)  # El valor por defecto es 4
    st.header("Condiciones Meteorológicas")
    cm_input = st.slider('', 0, 10, 10)  # El valor por defecto es 10

    # Botón para realizar la simulación
    if st.button('Calcular Tiempo de Semáforo'):
        ts_sim.input['Cantidad de vehiculos'] = qv_input
        ts_sim.input['Tiempo de espera'] = te_input
        ts_sim.input['Hora del dia'] = hd_input
        ts_sim.input['Condiciones meteorologicas'] = cm_input

        # Computar la salida
        ts_sim.compute()

# Mostrar el resultado
output_ts = ts_sim.output['Tiempo de semaforo']
st.write(f'El tiempo recomendado para el semáforo es: {output_ts} segundos.')

# no mostrar warning deprecation
st.set_option('deprecation.showPyplotGlobalUse', False)

#mostrar grafico resultado
st.pyplot(TS.view(sim=ts_sim))

    # Repetir para las demás variables de entrada y la variable de salida
    # ...

# Para mostrar las funciones de membresía sin realizar una simulación, puedes usar:
# st.pyplot(QV.view())

# Y se repite lo mismo para TE, HD, CM y TS
