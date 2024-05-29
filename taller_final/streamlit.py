import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import Nivel_2_Valoracion as valoracion
import modelos

def main():
    st.title("Sistema de para valoracion del riesgo")
    menu = ["Inicio", "Modelos", "Nivel 2: Valoración", "Nivel 3: Riesgo"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Inicio":
        st.subheader("Página de Inicio")
        st.write("Bienvenido al sistema de visualización de resultados.")
        st.write("Seleccione una opción del menú para visualizar los diferentes modelos y resultados.")
    
    elif choice == "Modelos":
        st.subheader("Modelos")
        modelos_app()

    elif choice == "Nivel 2: Valoración":
        st.subheader("Nivel 2: Valoración")
        valoracion_app()

    elif choice == "Nivel 3: Riesgo":
        st.subheader("Nivel 3: Riesgo")
        riesgo_app()


def valoracion_app():
    st.write("Este es el resultado del análisis de valoración de la situación.")
    # Asume que 'valoraciones_situacion.csv' ya está generado por el script Nivel_2_Valoracion.py
    valoraciones_df = pd.read_csv('valoraciones_situacion.csv')
    st.write(valoraciones_df.describe())
    
    # Visualización del histograma
    fig, ax = plt.subplots()
    ax.hist(valoraciones_df['Valoracion_Situacion'], bins=20, edgecolor='black')
    ax.set_title('Distribución de las Valoraciones de la Situación')
    ax.set_xlabel('Valoracion Situacion')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)
    
    # Visualización del boxplot
    fig, ax = plt.subplots()
    ax.boxplot(valoraciones_df['Valoracion_Situacion'], vert=False)
    ax.set_title('Boxplot de las Valoraciones de la Situación')
    ax.set_xlabel('Valoracion Situacion')
    st.pyplot(fig)

    st.write(" Resultados Dester-shaper.")
    resultados = pd.read_csv('resultados_dempster_shafer.csv')
    st.write(resultados)
    

def riesgo_app():
    st.write("Este es el resultado del análisis de riesgo.")
    # Asume que 'salidas_fis.csv' ya está generado por el script Nivel_3_Riesgo.py
    salidas_fis = pd.read_csv('salidas_fis.csv')
    st.write(salidas_fis.describe()) 

    # Visualización del riesgo de discrepancia
    fig, ax = plt.subplots()
    ax.hist(salidas_fis['Riesgo_Discrepancia'], bins=20, edgecolor='black')
    ax.set_title('Distribución del Riesgo de Discrepancia')
    ax.set_xlabel('Riesgo Discrepancia')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

    st.write(" Resultados Dester-shaper.")
    resultados3 = pd.read_csv('resultados_nivel3.csv')
    st.write(resultados3)

def modelos_app():
    st.write("Este es el resultado del análisis de modelos.")
    # Asume que 'predicciones_demanda.csv' y 'predicciones_impacto_promocion.csv' ya están generados por el script modelos.py
    demanda_df = pd.read_csv('predicciones_demanda.csv')
    impacto_promocion_df = pd.read_csv('predicciones_impacto_promocion.csv')
    inventario_rfid_df = pd.read_csv('predicciones_inventario_rfid.csv')
    
    st.write("Predicciones de Demanda")
    st.write(demanda_df.head())
    
    st.write("Predicciones del Impacto de la Promoción")
    st.write(impacto_promocion_df.head())
    
    st.write("Predicciones del Inventario RFID")
    st.write(inventario_rfid_df.head())
    
    # Gráficos
    fig, ax = plt.subplots()
    ax.hist(demanda_df['Demanda_Predicha'], bins=20, edgecolor='black')
    ax.set_title('Distribución de la Demanda Predicha')
    ax.set_xlabel('Demanda Predicha')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)
    
    fig, ax = plt.subplots()
    ax.hist(impacto_promocion_df['Impacto_Promocion'], bins=20, edgecolor='black')
    ax.set_title('Distribución del Impacto de la Promoción')
    ax.set_xlabel('Impacto Promocion')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)
    
    fig, ax = plt.subplots()
    ax.hist(inventario_rfid_df['Inventario_RFID'], bins=20, edgecolor='black')
    ax.set_title('Distribución del Inventario RFID')
    ax.set_xlabel('Inventario RFID')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
