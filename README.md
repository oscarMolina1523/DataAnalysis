<h1 align="left">Analisis de Mineria de Datos con Diferentes ejemplos reales</h1>

<h2 align="left">🛒 Market Basket Analysis con Apriori</h1>
###

<div align="center">
  <img src="https://i.ibb.co/F44kqcNC/data-Analits.png" alt="data-Analits" border="0">
</div>

###

<p align="left">Este proyecto implementa un <strong>"análisis de canasta de mercado"</strong> (Market Basket Analysis) utilizando el algoritmo <strong>"Apriori"</strong> en Python.  <br>El objetivo es descubrir <strong>"reglas de asociación"</strong> entre productos a partir de transacciones simuladas, ayudando a encontrar patrones de compra que puedan usarse en estrategias de marketing, promociones o diseño de tiendas.</p>

###

<h2 align="left">📌 Funcionalidades</h2>

###

<p align="left">- Generación de "itemsets frecuentes" con el algoritmo Apriori.<br>- Obtención de "reglas de asociación" filtradas por:<br>  - "support"<br>  - "confidence"<br>  - "lift"<br>- Conversión de "frozenset" a etiquetas legibles (ej. Producto 15 → Producto 18).<br>- Visualización de resultados con:<br>  - "Gráfico de barras" (Top 10 reglas por "support").<br>  - "Gráfico de dispersión" ("confidence" vs "lift" con tamaño proporcional al "support").<br>- Interpretación práctica de reglas clave.</p>

###

<h2 align="left">⚙️ Tecnologías usadas</h2>

###

<p align="left">- Python 3.x<br>- [Pandas](https://pandas.pydata.org/)<br>- [mlxtend](http://rasbt.github.io/mlxtend/) (para "apriori" y "association_rules")<br>- Matplotlib</p>

###

<h2 align="left">🚀 Ejecución</h2>

###
```bash
#clonar este repositorio
git clone https://github.com/oscarMolina1523/DataAnalysis.git

#entrar a la carpeta
cd DataAnalysis

#instalar dependencias 
pip install -r requirements.txt

#correr el archivo de Market Basket
python -m market_basket_analysis.market_main
```
###

<h2 align="left">✨ Autor</h2>

###

<p align="left">Desarrollado por Oscar Molina<br>💼 Desarrollador Web<br>GitHub: @oscarMolina1523<br>linkedin: https://www.linkedin.com/in/oscar-molina-916195309</p>

###
