# pandas es la librería principal para trabajar con tablas de datos en Python
import pandas as pd
# matplotlib.pyplot permite crear gráficos
import matplotlib.pyplot as plt

# Creamos un diccionario con los datos: cada clave es el nombre de una columna
# y cada valor es una lista con los datos de esa columna (uno por tipo de colegio)
# Fuente: Centro de Estudios MINEDUC
data = {
    'tipo_colegio': ['Municipal', 'Particular Subvencionado', 'Particular Pagado',
                      'Corporación Admin. Delegada', 'Servicio Local de Educación'],
    'promovido': [701847, 1700220, 302878, 41052, 400176],
    'reprobado': [18634, 41717, 709, 2389, 12136],
    'trasladado': [60800, 124646, 8684, 4711, 37026],
    'retirado': [18907, 40698, 1871, 972, 14036],
    'total': [800492, 1911961, 315275, 49134, 463473]
}

# pd.DataFrame convierte el diccionario en una tabla (filas x columnas)
# como una hoja de cálculo, que guardamos en la variable df
df = pd.DataFrame(data)

# Mostramos la tabla en la consola para verificar que los datos cargaron bien
print(df)

# Calculamos tasas porcentuales dividiendo cada categoría por el total
# y multiplicando por 100. .round(1) redondea a 1 decimal.
# Usamos tasas (%) en vez de valores absolutos para poder comparar grupos
# de distinto tamaño (ej: 1.9M subvencionados vs 49K corp. delegada)
df['tasa_aprobacion'] = (df['promovido'] / df['total'] * 100).round(1)
df['tasa_reprobacion'] = (df['reprobado'] / df['total'] * 100).round(1)
df['tasa_retiro'] = (df['retirado'] / df['total'] * 100).round(1)

# Imprimimos solo las columnas relevantes para el análisis
# La notación df[['col1', 'col2']] selecciona un subconjunto de columnas
print("\n--- Tasas porcentuales ---")
print(df[['tipo_colegio', 'tasa_aprobacion', 'tasa_reprobacion', 'tasa_retiro']])

# Creamos una figura de 10x6 pulgadas (tamaño del lienzo del gráfico)
plt.figure(figsize=(10, 6))

# Gráfico de barras: eje X = tipo de colegio, eje Y = tasa de aprobación
plt.bar(df['tipo_colegio'], df['tasa_aprobacion'], color='steelblue')

# Etiqueta del eje Y
plt.ylabel('Tasa de aprobación (%)')

# Título del gráfico
plt.title('Tasa de aprobación escolar por tipo de dependencia administrativa - Chile 2025')

# Rotamos las etiquetas del eje X 20° para que no se superpongan
# ha='right' alinea el texto a la derecha del punto de rotación
plt.xticks(rotation=20, ha='right')

# Ajusta automáticamente los márgenes para que nada quede cortado
plt.tight_layout()

# Guarda el gráfico como archivo PNG en la misma carpeta donde corre el script
plt.savefig('tasa_aprobacion.png')

print("\nGráfico guardado como tasa_aprobacion.png")
