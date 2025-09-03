import numpy as np                      # operaciones numéricas (media, varianza, etc.)
import pandas as pd                     # estructuras tabulares (Series, DataFrame)
import matplotlib.pyplot as plt         # gráficos básicos
import seaborn as sns                   # gráficos estéticos y boxplots

# Muestra de edades 
edades = [18, 20, 22, 23, 25, 25, 26, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 40, 42, 45]

# 1. TENDENCIA CENTRAL
# la media se obtiene de la suma de todos los numeros entre el la cantidad de numeros que hay
#ejemplo si hay 3 numeros [1,2,3] el total es 6 y ahora dividir entre 3 porque tenemos 3 numeros 
#6/3 =2 esa es la media
media = np.mean(edades)   

#La mediana es el número que está justo en el centro de la lista 
#cuando los datos están ordenados de menor a mayor. Si tienes un número par 
#de datos, la mediana es el promedio de los dos números que quedan en el centro.
mediana = np.median(edades)        

#La moda es el número que aparece con más frecuencia en la lista. 
#Es como el valor "más popular".
#a pesar de que pueden existir varias modas en un arreglo 
#en este ejemplo voy a tomar la primera moda que se me aparezca
moda = pd.Series(edades).mode()[0]     

# Imprime resultados solo para verlos
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# 2. VARIABILIDAD
varianza = np.var(edades, ddof=1)      # varianza muestral (divisor n-1)
desviacion = np.std(edades, ddof=1)    # desviación estándar muestral
print("Varianza (muestra):", varianza)
print("Desviación estándar (muestra):", desviacion)

# --- 3. Tabla de frecuencias por intervalos de 5 años ---
ancho = 5
min_edad = min(edades)
max_edad = max(edades)

# Alineamos los bordes a múltiplos de 5 (para que las clases sean limpias)
inicio = (min_edad // ancho) * ancho    # p.ej. 18 -> 15
fin = (max_edad // ancho) * ancho       # 45 -> 45

# Creamos los bordes (incluye un borde extra para cerrar el último bin)
bordes = np.arange(inicio, fin + ancho + 1, ancho)

# pd.cut asigna cada edad a un bin; right=False hace intervalos [a, b)
cats = pd.cut(edades, bins=bordes, right=False, include_lowest=True)
frecuencias = cats.value_counts().sort_index()

# Etiquetas legibles para reporte: "15–19", "20–24", ...
etiquetas = [f"{bordes[i]}–{bordes[i+1]-1}" for i in range(len(bordes)-1)]

tabla = pd.DataFrame({
    "Intervalo (años)": etiquetas,
    "Frecuencia": frecuencias.values,
})
tabla["% relativo"] = (tabla["Frecuencia"] / len(edades) * 100).round(2)
tabla["Frec acumulada"] = tabla["Frecuencia"].cumsum()

print("\nTabla de frecuencias (5 años):")
print(tabla)

# --- 4. Histograma anotado (mismo binning que la tabla) ---
plt.figure(figsize=(8,5))
sns.histplot(edades, bins=bordes, kde=False, edgecolor='black')  # histograma con seaborn
plt.title("Histograma de edades (intervalos de 5 años)")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.xticks(bordes)

# Anotar conteos encima de cada barra (estético y útil para presentaciones)
for i, freq in enumerate(frecuencias.values):
    # ubicamos la x en el centro del bin: (left+right)/2
    left = bordes[i]
    right = bordes[i+1]
    x = (left + right) / 2
    plt.text(x, freq + 0.1, str(int(freq)), ha='center', va='bottom')

plt.tight_layout()
plt.show()
