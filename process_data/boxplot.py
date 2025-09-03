import matplotlib.pyplot as plt

# Datos
tiempos_entrega = [20, 22, 23, 25, 25, 26, 27, 28, 30, 40, 50]

# a) Boxplot
plt.figure(figsize=(8,6))
plt.boxplot(tiempos_entrega, vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='black'),
            medianprops=dict(color='red', linewidth=2),
            flierprops=dict(marker='o', markerfacecolor='orange', markersize=10, linestyle='none'))
plt.title("Boxplot: Tiempos de Entrega")
plt.ylabel("Minutos")
plt.grid(True)
plt.show()
