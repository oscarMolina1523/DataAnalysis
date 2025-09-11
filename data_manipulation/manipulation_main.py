import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Dataset inicial con valores ya imputados (usando el código anterior)
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Pedro', 'Sofía'],
    'Edad': [25.0, 31.6, 35.0, 29.0, 40.0, 31.0],
    'Genero': ['Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Mujer'],
    'Ingresos': [500.0, 1200.0, 1180.0, 700.0, 1500.0, 2000.0]
}
df = pd.DataFrame(data)

# Imputación (para asegurar que los datos estén limpios)
df['Edad'] = df['Edad'].fillna(df['Edad'].mean())
df['Ingresos'] = df['Ingresos'].fillna(df['Ingresos'].mean())

# Normalización (MinMaxScaler)
scaler_minmax = MinMaxScaler()
df[['Edad_norm', 'Ingresos_norm']] = scaler_minmax.fit_transform(df[['Edad', 'Ingresos']])

# Estandarización (StandardScaler)
scaler_std = StandardScaler()
df[['Edad_std', 'Ingresos_std']] = scaler_std.fit_transform(df[['Edad', 'Ingresos']])

# Preparar los datos para el gráfico
df_melted = pd.DataFrame({
    'Edad': df['Edad'],
    'Ingresos': df['Ingresos'],
    'Tipo': 'Original'
})
df_melted = pd.concat([df_melted, pd.DataFrame({
    'Edad': df['Edad_norm'],
    'Ingresos': df['Ingresos_norm'],
    'Tipo': 'Normalizado'
})])
df_melted = pd.concat([df_melted, pd.DataFrame({
    'Edad': df['Edad_std'],
    'Ingresos': df['Ingresos_std'],
    'Tipo': 'Estandarizado'
})])

plt.figure(figsize=(10, 8))
sns.scatterplot(data=df_melted, x='Edad', y='Ingresos', hue='Tipo', style='Tipo', s=150)
plt.title('Comparación de Normalización vs. Estandarización', fontsize=16)
plt.xlabel('Valor Transformado (Edad)', fontsize=12)
plt.ylabel('Valor Transformado (Ingresos)', fontsize=12)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.grid(True)
plt.show()


# Puntos Originales (Círculos Azules): 
# Estos puntos representan tus datos sin procesar.

# Puntos Normalizados (Cruces Naranjas): 
# La normalización (usando el método MinMaxScaler) escala tus datos a un rango fijo,
#  generalmente de 0 a 1. Como puedes ver en el gráfico, todas las cruces naranjas se 
# agrupan en un área cuadrada en la esquina superior derecha, con valores de 0 a 1 en ambos ejes. 
# Esto significa que el punto con el valor más bajo en cada columna fue escalado a 0, y el punto con
#  el valor más alto fue escalado a 1. La normalización es útil para algoritmos que necesitan que los 
# datos estén en un rango específico.

# Puntos Estandarizados (Cuadrados Verdes): 
# La estandarización (usando el método StandardScaler) transforma tus 
# datos para que tengan una media de 0 y una desviación estándar de 1.
#  Los cuadrados verdes están centrados alrededor del punto (0,0) en el gráfico.
#  Un valor de 0 indica que ese dato es el promedio del grupo, mientras que un valor 
# de 1 significa que está a una desviación estándar por encima del promedio. Este método es 
# ideal para algoritmos que asumen que los datos tienen una distribución normal.