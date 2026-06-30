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

# Gráfico profesional: tasa de reprobación
fig, ax = plt.subplots(figsize=(12, 6))

colores = ['#e74c3c' if x == df['tasa_reprobacion'].max()
           else '#2ecc71' if x == df['tasa_reprobacion'].min()
           else '#95a5a6' for x in df['tasa_reprobacion']]

bars = ax.bar(df['tipo_colegio'], df['tasa_reprobacion'],
              color=colores, edgecolor='white', linewidth=0.8)

# Anotaciones encima de cada barra
for bar, val in zip(bars, df['tasa_reprobacion']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f'{val}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Línea de promedio
promedio = df['tasa_reprobacion'].mean()
ax.axhline(promedio, color='#2c3e50', linestyle='--', linewidth=1.2, alpha=0.7)
ax.text(4.5, promedio + 0.08, f'Promedio: {promedio:.1f}%',
        ha='right', fontsize=9, color='#2c3e50')

ax.set_title('Tasa de reprobación escolar por dependencia administrativa\nChile 2025',
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Tasa de reprobación (%)', fontsize=11)
ax.set_ylim(0, 6)
ax.tick_params(axis='x', labelsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(rotation=15, ha='right')
plt.tight_layout()
plt.savefig('tasa_reprobacion.png', dpi=150, bbox_inches='tight')
print("Gráfico guardado")
