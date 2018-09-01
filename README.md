1. INTRODUCCIÓN
Morita es un software que permite realizar informes estadísticos en diseños experimentales de uno o
dos factores de manera rápida y expeditiva, extrayendo los datos directamente desde un archivo
Excel (.xlsx).

2. REQUISITOS

WINDOWS
Morita esta escrito Python 3. Por ello y con el objetivo de simplificar la descarga de dependencias,
es requisito descargar e instalar Anaconda3.
https://www.anaconda.com/download/#windows

LINUX
Dependencias requeridas:
Pandas
Matplotlib
Seaborn
Statsmodels
PyQt5

3. INSTALACIÓN
Simplemente copiar la carpeta Morita en el directorio que considere apropiado. La misma puede
descargarse desde el siguiente link.

https://github.com/M0r1t4/Morita

4. EJECUTAR EL PROGRAMA.

4.1. Bajo el sistema operativo Windows iniciar Anaconda Prompt, si se tratara de MacOS o
Linux abrir una Terminal.

4.2. Dirigirse a la ubicación donde hubiera almacenado la carpeta Morita en el punto 3.

4.3. Escribir o copiar el siguiente comando en la ventana Anaconda Prompt o la Terminal
(dependiendo el sistema operativo): “python morita.py” y luego presionar Enter.

5. MODO DE USO

5.1. Presionar el botón IMPORTAR y seleccionar el archivo .xlsx de interés.
En el visor inferior deberá visualizarse la siguiente frase: Archivo – “ruta del archivo” --
cargado exitosamente.

5.2. En el display SELECCIONAR PÁGINA, se desplegaran las hojas activas del documento.
Seleccionar la pagina que contenga los datos a analizar.
NOTA: El programa no leerá las celdas vacías, por lo cual se recomienda que todas las celdas
estén completas.

5.3. Presionar el botón CARGAR DATOS.
En el visor inferior deberá visualizarse la siguiente frase: Página -- “nombre de la página” --
seleccionada exitosamente.

5.4. Seleccionar las columnas de la tabla que se designaran como Variable Independiente,
Condicionante y Variable Dependiente.
NOTA: Si el diseño experimental es de solo un factor, seleccionar en Variable Independiente
una columna que contenga valores iguales y en Condición la columna con los niveles que
deseen analizarse.

5.5. Presionar el botón ANALIZAR.
En el visor inferior deberá visualizarse la siguiente frase: Informe generado exitosamente.
Directorio de almacenamiento: “ruta del archivo”.

6. INFORME

Luego de pulsar el botón ANALIZAR, automáticamente se generará un informe en formato .txt
dentro de la carpeta Morita. El nombre del archivo constara de 2 números consecutivos: el primero
correspondiente a la fecha de análisis y el segundo la hora.
Además se creará de forma independiente un layout conteniendo cuatro gráficos: un gráfico de
barras con desviación estándar, un gráfico de cajas, un gráfico de estilo violín, y un gráfico de
puntos.

7. BREVE INTERPRETACIÓN DE LOS RESULTADOS.

7.1. Tabla resumen: Se imprime en el informe la tabla resumida con las columnas seleccionadas
para: Variable Independiente, Condicionante y Variable Dependiente.

7.2. Estadística descriptiva: Se imprime la cantidad de datos (count), el promedio (mean), la
desviación estándar (std), el valor mínimo (min), el primer cuartil (25%), el segundo cuartil
(50%), el tercer cuartil (75%) y el valor máximo (max), para cada tratamiento.

7.3. Anova de una vía: Para cada una de las variables independientes se imprime el valor F y el
valor P.

7.4. Test de Kruskal Wallis: Para cada una de las variables independientes se imprime el valor
estadístico (es el primer valor dentro del paréntesis) y el valor P (el segundo valor dentro del
paréntesis).

7.5. Test de Tukey HSD: Para cada una de las variables independiente se imprime las
comparaciones de los t niveles. En caso de observarse en la (última) columna “reject” la
palabra “True” se rechaza la hipótesis nula, si se observase “False”, no.

7.6. Anova de dos vías: Se imprime el test de anova de dos vías, incluyendo interacción.

7.7. Test de Levene: Para cada una de las variables independientes se imprime el valor
estadístico (es el primer valor dentro del paréntesis) y el valor P (el segundo valor dentro del
paréntesis).

7.8. Test de Barlett: Para cada una de las variables independientes se imprime el valor
estadístico (es el primer valor dentro del paréntesis) y el valor P (el segundo valor dentro del
paréntesis).

7.9. Test de normalidad: Se utiliza la prueba de Shapiro Wilk. Para cada una de los niveles de
cada variable independiente se imprime el valor estadístico (primer valor dentro del paréntesis)
y el valor P (el segundo valor dentro del paréntesis).
