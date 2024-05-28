import pandas as pd
import numpy as np
import random

# Configurar el generador de números aleatorios
np.random.seed(42)
random.seed(42)

# Definir el número de registros
num_records = 10000

# Generar datos sintéticos para el inventario inicial
inventario_inicial = {
    'ProductoID': np.random.randint(1, 101, num_records),
    'Categoria': np.random.choice(['Camisetas', 'Pantalonetas', 'Busos'], num_records),
    'Precio': np.round(np.random.uniform(25000, 85000, num_records)),
    'Cantidad': np.random.randint(500, 1000, num_records),  # Asegurando una cantidad suficientemente alta
    'Estacion': np.random.choice(['Primavera', 'Verano', 'Otoño', 'Invierno'], num_records)
}

# Crear un DataFrame
df_inventario = pd.DataFrame(inventario_inicial)

# Generar Ventas Históricas basadas en la cantidad
df_inventario['VentasHistoricas'] = df_inventario['Cantidad'] * np.random.uniform(0.3, 0.5, num_records)

# Generar Demanda basada en Ventas Históricas y cantidad disponible
df_inventario['Demanda'] = np.minimum(df_inventario['Cantidad'], df_inventario['VentasHistoricas'] * np.random.uniform(0.8, 1.2, num_records))

# Calcular Ventas Durante Promoción
df_inventario['Promocion'] = np.random.choice([0, 1], num_records)
df_inventario['VentasDurantePromocion'] = np.where(df_inventario['Promocion'] == 1,
                                                   df_inventario['VentasHistoricas'] * np.random.uniform(1.1, 1.3, num_records),
                                                   df_inventario['VentasHistoricas'] * np.random.uniform(0.7, 0.9, num_records))

# Calcular Ventas Post Promoción
df_inventario['VentasPostPromocion'] = df_inventario['VentasDurantePromocion'] * np.random.uniform(0.6, 0.8, num_records)

# Calcular Inventario Inicial para garantizar que no sea negativo ni cero
df_inventario['InventarioInicial'] = df_inventario['Cantidad'] + df_inventario['VentasDurantePromocion'] + df_inventario['VentasPostPromocion']

# Calcular Inventario Inicial en Recepción, Almacenamiento y Ventas
df_inventario['InventarioRecepcion'] = df_inventario['InventarioInicial'] * np.random.uniform(0.95, 1.05, num_records)
df_inventario['InventarioAlmacenamiento'] = df_inventario['InventarioRecepcion'] - df_inventario['VentasDurantePromocion']
df_inventario['InventarioVentas'] = df_inventario['InventarioAlmacenamiento'] - df_inventario['VentasPostPromocion']

# Asegurar que ningún valor de inventario sea negativo ni cero
df_inventario['InventarioRecepcion'] = df_inventario['InventarioRecepcion'].apply(lambda x: max(x, 1))
df_inventario['InventarioAlmacenamiento'] = df_inventario['InventarioAlmacenamiento'].apply(lambda x: max(x, 1))
df_inventario['InventarioVentas'] = df_inventario['InventarioVentas'].apply(lambda x: max(x, 1))

# Guardar el DataFrame actualizado en un archivo CSV
df_inventario.to_csv('inventario_con_datos_rfid.csv', index=False, encoding='utf-8-sig')

print("Datos guardados en 'inventario_con_datos_rfid.csv'")
