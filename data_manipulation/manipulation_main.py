import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

# Dataset inicial con problemas
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Pedro', 'Sofía'],
    'Edad': [25, np.nan, 35, 29, 40, 31],
    'Genero': ['Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Mujer'],
    'Ingresos': [500, 1200, np.nan, 700, 1500, 2000]
}
df = pd.DataFrame(data)
print("  Dataset original:")
print(df)
print("-" * 30)

# 1. Imputación de valores faltantes
df['Edad'].fillna(df['Edad'].mean(), inplace=True)
df['Ingresos'].fillna(df['Ingresos'].mean(), inplace=True)
print("\n  Después de imputación de valores faltantes:")
print(df)
print("-" * 30)

# 2. Codificación de variables categóricas con Label Encoding
le = LabelEncoder()
df['Genero_encoded'] = le.fit_transform(df['Genero'])
# Eliminamos la columna original 'Genero' para evitar redundancia
df.drop('Genero', axis=1, inplace=True)
print("\n  Después de codificación Label Encoding:")
print(df)
print("-" * 30)

# 3. Discretización de ingresos en categorías
df['SegmentoIngresos'] = pd.cut(
    df['Ingresos'],
    bins=[0, 800, 1500, 3000],
    labels=['Bajo', 'Medio', 'Alto']
)
print("\n Después de discretización de ingresos:")
print(df[['Ingresos', 'SegmentoIngresos']])
print("-" * 30)

# 4. Normalización y estandarización
# Las columnas 'Genero' y 'Nombre' no son numéricas para escalar, por eso seleccionamos las correctas
numeric_cols = ['Edad', 'Ingresos']
scaler_minmax = MinMaxScaler()
scaler_std = StandardScaler()
df[[f'{col}_norm' for col in numeric_cols]] = scaler_minmax.fit_transform(df[numeric_cols])
df[[f'{col}_std' for col in numeric_cols]] = scaler_std.fit_transform(df[numeric_cols])

print("\n  Después de normalización y estandarización:")
print(df[['Edad', 'Ingresos', 'Edad_norm', 'Ingresos_norm', 'Edad_std', 'Ingresos_std']])