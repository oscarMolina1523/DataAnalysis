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
media = np.mean(edades)   #output=30.8

#La mediana es el número que está justo en el centro de la lista 
#cuando los datos están ordenados de menor a mayor. Si tienes un número par 
#de datos, la mediana es el promedio de los dos números que quedan en el centro.
mediana = np.median(edades)   #output =30.5

#La moda es el número que aparece con más frecuencia en la lista. 
#Es como el valor "más popular".
#a pesar de que pueden existir varias modas en un arreglo 
#en este ejemplo voy a tomar la primera moda que se me aparezca
moda = pd.Series(edades).mode()[0]    #output=25

# Imprime resultados solo para verlos
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# 2. VARIABILIDAD

#La varianza muestral mide el promedio de la distancia de cada número a la media, 
#pero al cuadrado. Al elevar al cuadrado las distancias, 
#los valores negativos se vuelven positivos y los valores más alejados de la media tienen un peso mayor.
#dividiremos por n-1 (el número total de datos menos 1)
#ej: ya sabemos que nuestra media es 30.8 porque lo calculamos en las lineas anteriores
#ahora resta la media a cada número y eleva el resultado al cuadrado
#(18−30.8)^2=(−12.8)^2 =163.84 y asi con cada uno de los numeros
#luego sumaras todos los resultados de la operacion anterior
#y por ultimo divides entre el numero total de elementos -1 
#en nuestro caso hay 20 datos -1 es =19
varianza = np.var(edades, ddof=1)     #output=75.73

#la desviacion estandar es la raíz cuadrada de la varianza. 
#Nos dice, en promedio, qué tan lejos está cada dato de la media. 
#Un valor pequeño significa que los datos están agrupados cerca de la media,
#y un valor grande significa que están más dispersos.
#La desviación estándar muestral es aproximadamente 8.7. Esto significa que, en promedio, 
#las edades de las personas en tu grupo se desvían alrededor de 8.7 años de la edad media de 30.8.
desviacion = np.std(edades, ddof=1)    # output=8.697
print("Varianza (muestra):", varianza)
print("Desviación estándar (muestra):", desviacion)

# 3. TABLA DE FRECUENCIAS CON INTERVALOS DE 5 AÑOS
ancho = 5
min_edad = min(edades)
max_edad = max(edades)

# Alineamos los bordes a múltiplos de 5 
#las // lo que hacen es redondear hacia abajo el resultado
#ej: 18//5. La división normal sería 3.6. La división entera redondea hacia abajo a 3.
inicio = (min_edad // ancho) * ancho    # p.ej. 18 -> 15
fin = (max_edad // ancho) * ancho       # 45 -> 45

# Creamos los bordes (incluye un borde extra para cerrar el último bin)
#lo que hace es crear una secuencia de numeros, el primer parametro es de donde inicia, 
#el segundo es hasta donde va llegar es de 51 pero sin incluirlo a el por lo que realmente llegara a 50
#y el ancho de cada secuencia en este caso 5
bordes = np.arange(inicio, fin + ancho + 1, ancho)

# pd.cut asigna cada edad a un grupo correcto
#recibe los datos que son [edades], asigna limite con [bordes]
#right=False es de tipo [a, b] es decir el dato de la izquierda se asigna pero el de la derecha no
#Por ejemplo, el primer grupo es de [15, 20). Esto significa que incluye 
#el 15, el 16, el 17, el 18 y el 19, pero no el 20. El número 20 irá en el siguiente grupo.
#include_lowest=True asegura que si el valor más pequeño de tus datos (en este caso, 18)
# es igual al primer borde de la clase (15), el valor se incluya en el primer grupo.
cats = pd.cut(edades, bins=bordes, right=False, include_lowest=True)

#el value_counts() cuenta cuantas edades caen en cada categoria
#y el sort_index() ordena de menor a mayor
frecuencias = cats.value_counts().sort_index()

# Etiquetas legibles para reporte: "15–19", "20–24", ...
#es decir el bucle for recorre de 0 a 6 ya que bordes-1 es 7 y el ultimo valor no se toma en cuenta
#luego usando el indice accede al valor de cada ciclo es este caso bordes[i] es 15 
#y bordes[i+1] es 20 y luego restas 1 se convierte en 19 porque tenemos nuemeros de 15-19 
#ya que el proximo ciclo empieza en 20
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
