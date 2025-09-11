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