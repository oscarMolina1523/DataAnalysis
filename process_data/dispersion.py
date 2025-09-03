import matplotlib.pyplot as plt

# Datos
publicidad = [2, 4, 6, 8, 10]  # en miles
ventas = [15, 25, 35, 50, 65]  # en miles

# a) Diagrama de dispersión
plt.figure(figsize=(8,6))
plt.scatter(publicidad, ventas, color='blue', s=100)  # s = tamaño de los puntos
plt.title("Diagrama de dispersión: Publicidad vs Ventas")
plt.xlabel("Gastos en Publicidad (miles)")
plt.ylabel("Ventas (miles)")
plt.grid(True)
plt.show()
