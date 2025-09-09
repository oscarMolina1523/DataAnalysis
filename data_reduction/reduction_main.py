import pandas as pd 
import numpy as np 
from sklearn.feature_selection import SelectKBest, chi2 
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt 

# np.random.seed(42) 

# data = { 
#     "edad": np.random.randint(18, 65, 100), 
#     "ingresos": np.random.randint(300, 5000, 100), 
#     "gasto_salud": np.random.randint(100, 2000, 100), 
#     "horas_trabajo": np.random.randint(20, 60, 100), 
#     "horas_estudio": np.random.randint(0, 30, 100), 
#     "actividad_fisica": np.random.randint(0, 10, 100), 
#     "consumo_frutas": np.random.randint(0, 7, 100), 
#     "consumo_alcohol": np.random.randint(0, 5, 100), 
#     "diagnostico": np.random.randint(0, 2, 100)  # Variable objetivo 
# } 

# df = pd.DataFrame(data) 
# df.to_csv("data_reduction/data/dataset_reduccion.csv", index=False) 

df= pd.read_csv("data_reduction/data/dataset_reduccion.csv")
X = df.drop("diagnostico", axis=1) 

y = df["diagnostico"] 

selector = SelectKBest(score_func=chi2, k=2) 

X_new = selector.fit_transform(X, y) 

print("Características seleccionadas:") 

print(X.columns[selector.get_support()]) 

X_scaled = StandardScaler().fit_transform(X) 


pca = PCA(n_components=2) 

X_pca = pca.fit_transform(X_scaled) 

  

print("Varianza explicada por los componentes:", pca.explained_variance_ratio_) 

print("Nuevas características (primeras 2 filas):") 

print(X_pca[:2]) 

plt.scatter(X_pca[:,0], X_pca[:,1], c=y, cmap="viridis") 

plt.xlabel("Componente Principal 1") 

plt.ylabel("Componente Principal 2") 

plt.title("Visualización de datos reducidos con PCA") 

plt.show() 