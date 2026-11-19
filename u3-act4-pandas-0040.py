import pandas as pd
import matplotlib.pyplot as plt
## NL = 17  Herramientas especializadas
## Hugo Fabian NC 0040
# 1. Crear diccionario con datos de herramientas del taller
herramientas_taller = {
    'id_herramienta': [801, 802, 803, 804, 805, 806],
    'nombre': ['Escáner OBD2', 'Torquímetro', 'Gato hidráulico', 'Compresor aire', 'Multimetro digital', 'Juego de dados'],
    'marca': ['Launch', 'Truper', 'Blackhawk', 'Truper', 'Fluke', 'Stanley'],
    'tipo': ['Electronica', 'Manual', 'Hidraulica', 'Neumatica', 'Electronica', 'Manual'],
    'fecha_compra': ['2022-05-01', '2021-03-15', '2020-08-10', '2019-11-20', '2023-01-10', '2021-06-05'],
    'costo': [8000, 1200, 3500, 15000, 2500, 1800],
    'estado': ['Bueno', 'Excelente', 'Regular', 'Bueno', 'Excelente', 'Bueno'],
    'ubicacion': ['Caja herramientas', 'Caja herramientas', 'Foso 1', 'Area compresor', 'Mesa trabajo', 'Caja herramientas'],
    'responsable': ['Roberto', 'Luis', 'Carlos', 'Fernando', 'Jorge', 'Miguel'],
    'requiere_calibracion': [True, True, False, True, True, False]
}

print("Análisis Exploratorio de Datos")
print("Por Hugo Fabian NC 0040")
print("Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(herramientas_taller)
print("\n--- TABLA ORIGINAL DE HERRAMIENTAS ---")
print(df)

# 3. Exportar los datos a CSV
print("-+-+-+-+-+- Convertir el DataFrame en archivo CSV +-+-+-+-+-")
df.to_csv(
    'herramientas_taller_0040.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("8.-+-+-+-+- Leer los datos desde el archivo CSV -+-+-+-+-+-")
print('herramientas_taller_0040.csv')

# 4. Leer el archivo CSV
df = pd.read_csv('herramientas_taller_0040.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("+-+-+-+-+-+ 9. Análisis Exploratorio de Datos -+-+-+-+-+")
# 5. Primeros y últimos registros
print("\n1. PRIMEROS REGISTROS (Head):")
print(df.head(3))  # Muestra los primeros 3
print("\n2. ÚLTIMOS REGISTROS (Tail):")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+-+-+-+-+ 6. Dimensiones y estructura -+-+-+-+-+")
print(df)  # Mostrar tabla matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("\n7. ESTADÍSTICAS DESCRIPTIVAS:")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Tipos de herramientas únicos:", df['tipo'].unique())

# 8. Análisis específico
print(df)
print("-------------------------------")
print("\n11. HERRAMIENTAS POR TIPO:")
print(df['tipo'].value_counts())

print("\n12. PROMEDIO DE COSTO: $", df['costo'].mean())
print("13. COSTO MÁXIMO: $", df['costo'].max())
print("14. COSTO MÍNIMO: $", df['costo'].min())

# 9. Ordenamiento, filtrado y agrupación
print("\nOrdenamiento, filtrado y agrupación")
print("+-+-+-+--+-\n15. HERRAMIENTAS ORDENADAS POR COSTO (Mayor a menor): +-+-+-+-+-+")
print(df.sort_values(by='costo', ascending=False))

print("\n16. HERRAMIENTAS CON COSTO MAYOR A $3,000:")
filtro = df[df['costo'] > 3000]
print(filtro)

print("\n17. RESUMEN POR TIPO DE HERRAMIENTA:")
resumen = df.groupby('tipo').agg(
    cantidad=('id_herramienta', 'count'),
    costo_promedio=('costo', 'mean'),
    costo_maximo=('costo', 'max')
)
print(resumen)

# 18. Gráfica de barras: Herramientas por tipo
print("18. Gráfica de barras: Herramientas por tipo")
conteo = df['tipo'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Herramientas por tipo - Hugo Fabian NC 0040 NL 17')
plt.xlabel('Tipo de herramienta')
plt.ylabel('Cantidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Costo por herramienta
plt.figure(figsize=(9, 5))
plt.bar(df['nombre'], df['costo'], color='lightgreen')
plt.title('Costo por herramienta - Hugo Fabian NC 0040 NL 17')
plt.xlabel('Herramienta')
plt.ylabel('Costo en pesos')
plt.xticks(rotation=15)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de costos
plt.figure(figsize=(8, 5))
plt.hist(df['costo'], bins=4, color='orange', edgecolor='black')
plt.title('Distribución de costos de herramientas - Hugo Fabian NC 0040 NL 17')
plt.xlabel('Costo ($)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Extraer el año de compra como variable numérica para análisis temporal y correlación
df['anio_compra'] = pd.to_datetime(df['fecha_compra']).dt.year

# 21. Gráfica de dispersión: Año de compra vs Costo
plt.figure(figsize=(8, 5))
plt.scatter(df['anio_compra'], df['costo'], color='red', s=100)
plt.title('Relación entre año de compra y costo - Hugo Fabian NC 0040 NL 17')
plt.xlabel('Año de compra')
plt.ylabel('Costo ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de costos
plt.figure(figsize=(7, 5))
plt.boxplot(df['costo'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de costos (Boxplot) - Hugo Fabian NC 0040 NL 17')
plt.ylabel('Costo ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(8, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas - Hugo Fabian NC 0040 NL 17')
plt.tight_layout()
plt.show()