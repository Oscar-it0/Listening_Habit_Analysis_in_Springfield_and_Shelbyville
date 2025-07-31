#!/usr/bin/env python
# coding: utf-8

# **Comentario del Revisor**
# 
# Hola!
# 
# Soy Juan Manuel Romero, pero siéntete libre de llamarme Juanma. Soy code reviewer en Tripleten y hoy estaré revisando tu entrega.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión. 
# 
# Solo un aviso rápido: cuando estés revisando el proyecto, por favor deja mis comentarios originales tal como están. De esta manera, podemos seguir fácilmente el progreso y asegurarnos de que no se nos pase nada por alto. Y, si realizas algún cambio basado en mis comentarios, sería genial si pudieras resaltar esas actualizaciones para que se destaquen.
# 
# Puedes encontrar mis comentarios en cajas verdes, amarillas o rojas como estas:
# 
# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor</b> <a class="tocSkip"></a>
# 
# Éxito. Todo se ha hecho correctamente.
# 
# </div>
# 
# 
# <div class="alert alert-block alert-warning"> 
# <b>Comentario del Revisor</b> <a class="tocSkip"></a>
# 
# Observaciones. Algunas recomendaciones.
# 
# </div> 
# 
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del Revisor</b> <a class="tocSkip"></a>
# 
# Requiere corrección. El bloque requiere algunas correcciones. El trabajo no puede ser aceptado con los comentarios en rojo.
# 
# </div>
# 
# Puedes responderme usando esto:
# 
# <div class="alert alert-block alert-info"> <b>Respuesta del estudiante.</b> <a class="tocSkip"></a> </div>

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypothesis)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar la hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba la hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar la hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos.
#  2. Preprocesamiento de datos.
#  3. Prueba de hipótesis.
# 
# 
# 
# 
# 
# 
# 

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[1]:


# Importar pandas
import pandas as pd


# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[2]:


# Leer el archivo y almacenarlo en df
df=pd.read_csv('/datasets/music_project_en.csv')


# Muestra las 10 primeras filas de la tabla:

# In[3]:


# Obtener las 10 primeras filas de la tabla df
df.head(10)


# Obtén la información general sobre la tabla con un comando. Conoces el método que muestra la información general que necesitamos.

# In[4]:


# Obtener la información general sobre nuestros datos
df.info()


# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Excelente trabajo!
# 
# </div>

# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Almacenan los mismos tipos de datos: `object`.
# 
# Según la documentación:
# - `' userID'`: identificador del usuario o la usuaria;
# - `'Track'`: título de la canción;
# - `'artist'`: nombre del artista;
# - `'genre'`: género de la pista;
# - `'City'`: ciudad del usuario o la usuaria;
# - `'time'`: la hora exacta en la que se reprodujo la canción;
# - `'Day'`: día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. Es preferible utilizar snake_case.
# 
# 
# 

# ### Escribe observaciones de tu parte. Estas son algunas de las preguntas que pueden ser útiles: <a id='data_review_conclusions'></a>
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`
# Las columnas de importancia relevante son ‘user_id’, ‘city’ y ‘day’, según el objetivo principal “La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad”.
# Debemos considerar que el valor ‘time’ parece numérico pero no es un rango de tiempo sino la etiqueta de la hora específica en que se llevó a cabo la escucha.
# Podríamos revisar las columnas de ‘genre’ (no es prioridad para el presente caso), ‘city’ y ‘day’ para saber qué datos almacenan y si cuentan con errores ortográficos o diferente escritura del mismo género ciudad o día para corregir y unificar los listados de datos. Aunque quizá la recolección de datos de esta tabla sea obtenida de sistemas parametrizados y no por ingresos de los usuarios, no sea tan necesario un paso como éste.
# ‘genre’ considera 268 géneros diferentes
# ‘city’ sólo considera un total de 2 ciudades ['Shelbyville' 'Springfield']
# ‘day’ considera 3 días ['Friday' 'Monday' 'Wednesday']
# 
# 
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestra hipótesis o necesitamos más información?`
# Sí son suficientes
# 
# No contamos con valores numéricos que tengamos que usar en operaciones aritméticas ya que, para los objetivos establecidos, no es necesario por lo que creo que mantener todas las columnas como ‘object’ es correcto. En caso de querer obtener información secundaria como la hora del día en que ocurren las reproducciones, se podría cambiar el tipo de dato de la columna a numérico con el fin de evaluar el momento del día, pero hasta ahora no es necesario.
# 
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
# Las columnas ‘track’, ‘artist’ y ‘genre’ cuentan con valores ausentes. En las tres columnas podremos complementar los datos ausentes con algún dato aleatorio como ‘other’ ya que no interfieren para el objetivo principal.
# Determinar cuántas filas se duplican exactamente ya que no tendría sentido tener mas de una fila con el mismo usuario escuchando lo mismo a la misma hora, por lo que muy probablemente estás filas se deban desechar.
# Al parecer 3,826 líneas se encuentran duplicadas.
# Después de eliminar las líneas idénticas, se podrían determinar filas duplicadas considerando ‘user’ y ‘time’ ya que es muy poco probable el caso de escuchar dos pistas al mismo tiempo.
# 

# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Excelentes observaciones Oscar! Felicidades
# 
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla (los nombres de las columnas):

# In[5]:


# Muestra los nombres de las columnas
print(df.columns)


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * Todos los caracteres deben ser minúsculas.
# * Elimina los espacios.
# * Si el nombre tiene varias palabras, utiliza snake_case.

# Anteriormente, aprendiste acerca de la forma automática de cambiar el nombre de las columnas. Vamos a aplicarla ahora. Utiliza el bucle for para iterar sobre los nombres de las columnas y poner todos los caracteres en minúsculas. Cuando hayas terminado, vuelve a mostrar los encabezados de la tabla:

# In[6]:


# Bucle en los encabezados poniendo todo en minúsculas
new_column_name=[]
for old_name in df.columns:
    name_lowered=old_name.lower()
    new_column_name.append(name_lowered)

df.columns=new_column_name
print(df.columns)


# Ahora, utilizando el mismo método, elimina los espacios al principio y al final de los nombres de las columnas e imprime los nombres de las columnas nuevamente:

# In[7]:


# Bucle en los encabezados eliminando los espacios
new_column_name_2=[]
for old_name in df.columns:
    name_stripped=old_name.strip()
    new_column_name_2.append(name_stripped)

df.columns=new_column_name_2
print(df.columns)


# Necesitamos aplicar la regla de snake_case a la columna `userid`. Debe ser `user_id`. Cambia el nombre de esta columna y muestra los nombres de todas las columnas cuando hayas terminado.

# In[8]:


# Cambiar el nombre de la columna "userid"
columns_new={
    'userid':'user_id',
    'track':'track',
    'artist':'artist',
    'genre':'genre',
    'city':'city',
    'time':'time',
    'day':'day',
    }

df.rename(columns=columns_new,inplace=True)
print(df.columns)


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[9]:


# Comprobar el resultado: la lista de encabezados
print(df.columns)


# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Impecable! Todo correcto
# 
# </div>

# [Volver a Contenidos](#back)

# ### Valores ausentes <a id='missing_values'></a>
#  Primero, encuentra el número de valores ausentes en la tabla. Debes utilizar dos métodos en una secuencia para obtener el número de valores ausentes.

# In[10]:


# Calcular el número de valores ausentes
df.info()
print("Hay",df['track'].isna().sum(),"valores ausentes en track")
print("Hay",df['artist'].isna().sum(),"valores ausentes en artist")
print("Hay",df['genre'].isna().sum(),"valores ausentes en genre")


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en las columnas `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Como mostramos anteriormente en las lecciones, la mejor forma de hacerlo es crear una lista que almacene los nombres de las columnas donde se necesita el reemplazo. Luego, utiliza esta lista e itera sobre las columnas donde se necesita el reemplazo haciendo el propio reemplazo.

# In[11]:


# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
columns_to_replace = ['track','artist','genre']
for col in columns_to_replace:
    df[col].fillna('unknown',inplace=True)


# Ahora comprueba el resultado para asegurarte de que después del reemplazo no haya valores ausentes en el conjunto de datos. Para hacer esto, cuenta los valores ausentes nuevamente.

# In[12]:


# Contar valores ausentes
df.info()
print("Hay",df['track'].isna().sum(),"valores ausentes en track")
print("Hay",df['artist'].isna().sum(),"valores ausentes en artist")
print("Hay",df['genre'].isna().sum(),"valores ausentes en genre")


# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Excelente trabajo con esos valores ausentes
# 
# </div>

# [Volver a Contenidos](#back)

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla. Una vez más, debes aplicar dos métodos en una secuencia para obtener la cantidad de duplicados explícitos.

# In[13]:


# Contar duplicados explícitos
print(df.duplicated().sum())


# Ahora, elimina todos los duplicados. Para ello, llama al método que hace exactamente esto.

# In[14]:


# Eliminar duplicados explícitos
df=df.drop_duplicates()


# Comprobemos ahora si eliminamos con éxito todos los duplicados. Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[15]:


# Comprobar de nuevo si hay duplicados
print("Existen",df.duplicated().sum(),"duplicados explícitos")
print()
print("Número de registros en información original:",65079,"\nMenos duplicados explícitos:",3826,"\nTotal:",65079-3826)
print()
df.info()


# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Todo correcto
# 
# </div>

# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para ello:
# * Extrae la columna `genre` del DataFrame.
# * Llama al método que devolverá todos los valores únicos en la columna extraída.
# 

# In[16]:


# Inspeccionar los nombres de géneros únicos
print(df['genre'].sort_values().unique())
print(df['genre'].nunique())


# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, crea una función llamada `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=`: esta es una lista que contiene todos los valores que necesitas reemplazar.
# * `correct_genre=`: este es un string que vas a utilizar como reemplazo.
# 
# Como resultado, la función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplazar cada valor de la lista `wrong_genres` por el valor en `correct_genre`.
# 
# Dentro del cuerpo de la función, utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos, extrae la columna `'genre'` y aplica el método `replace` para hacer correcciones.

# In[17]:


# Función para reemplazar duplicados implícitos
wrong_genres=['hip','hop','hip-hop']
correct_genre='hiphop'
def replace_wrong_genres(data,column,wrong_values,correct_values):
    for wrong_value in wrong_values:
        data[column]=data[column].replace(wrong_values,correct_values)
    return data


# Ahora, llama a `replace_wrong_genres()` y pásale tales argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[18]:


# Eliminar duplicados implícitos
wrong_genres=['hip','hop','hip-hop']
correct_genre='hiphop'

df=replace_wrong_genres(df,'genre',wrong_genres,correct_genre)


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[19]:


# Comprobación de duplicados implícitos
print(df['genre'].sort_values().unique())
print(df['genre'].nunique())


# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Muy buen trabajo!
# 
# </div>

# [Volver a Contenidos](#back)

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`
# Necesito descubrir más herramientas para analizar un listado de 269 ya que posiblemente pueda haber más casos como el de hiphop.

# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Exacto! En la vida real, taréas como estas pueden llevar mucho tiempo
# 
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypothesis'></a>

# ### Hipótesis: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Recuerda las etapas dividir-aplicar-combinar de las que hablamos anteriormente en la lección. Tu objetivo ahora es agrupar los datos por ciudad, aplicar el método apropiado para contar durante la etapa de aplicación y luego encontrar la cantidad de canciones reproducidas en cada grupo especificando la columna para obtener el recuento.
# 
# A continuación se muestra un ejemplo de cómo debería verse el resultado final:
# `df.groupby(by='....')['column'].method()`Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[20]:


# Contar las canciones reproducidas en cada ciudad
print(df.groupby(by='city')['track'].count())


# `Comenta tus observaciones aquí`
# Considerando que ya no se tienen filas duplicadas, cada fila considera cada vez que una canción fue escuchada en cada ciudad.

# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Correcto
# 
# </div>

# Ahora agrupemos los datos por día de la semana y encontremos el número de canciones reproducidas el lunes, miércoles y viernes. Utiliza el mismo método que antes, pero ahora necesitamos una agrupación diferente.
# 

# In[21]:


# Calcular las canciones reproducidas en cada uno de los tres días
print(df.groupby(by='day')['track'].count())


# `Comenta tus observaciones aquí`
# Señala el numero de veces que una canción fue puesta en marcha por cada día.

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'` (lunes).
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[22]:


# Declara la función number_tracks() con dos parámetros: day= y city=.

    # Almacena las filas del DataFrame donde el valor en la columna 'day' es igual al parámetro day=

    # Filtra las filas donde el valor en la columna 'city' es igual al parámetro city=

    # Extrae la columna 'user_id' de la tabla filtrada y aplica el método count()

    # Devolve el número de valores de la columna 'user_id'


# In[22]:


Day_1='Monday'
Day_2='Wednesday'
Day_3='Friday'
City_1='Springfield'
City_2='Shelbyville' 

def number_tracks(Data,Day,City):
    df_filtered=Data[(Data['day']==Day)&(Data['city']==City)]
    user_count=df_filtered['user_id'].count()
    return f"{user_count} pistas reproducidas el {Day} en {City}."


# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[23]:


# El número de canciones reproducidas en Springfield el lunes
print(number_tracks(df,Day_1,City_1))


# In[24]:


# El número de canciones reproducidas en Shelbyville el lunes
print(number_tracks(df,Day_1,City_2))


# In[26]:


# El número de canciones reproducidas en Springfield el miércoles
print(number_tracks(df,Day_2,City_1))


# In[27]:


# El número de canciones reproducidas en Shelbyville el miércoles
print(number_tracks(df,Day_2,City_2))


# In[28]:


# El número de canciones reproducidas en Springfield el viernes
print(number_tracks(df,Day_3,City_1))


# In[29]:


# El número de canciones reproducidas en Shelbyville el viernes
print(number_tracks(df,Day_3,City_2))


# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Impecable! Todos los resultados son correctos. Muy buena forma de mostrar los resultados
# 
# </div>

# **Conclusiones**
# 
# `Comenta si la hipótesis es correcta o se debe rechazar. Explica tu razonamiento.`
# Se entiende que al no haber valores cuantitativos, los resultrados mostrados se determinan a partir del conteo de valores categóricos, lo que significa contar cada renglón como una unidad. El no localizar registros duplicados significaría una alteración a los resultados obtenidos por lo que es recomendable agotar los recursos en la limpieza de datos.

# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Correcto
# 
# </div>

# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resume aquí tus conclusiones sobre la hipótesis.`
# Existen variaciones en cuanto al número de escuchas por cada ciudad. 
# En el caso de Springfield el día miércoles decrece un 30% considerando el promedio de 15,800 escuchas en lunes y viernes.
# Por otro lado, Shelbyville actúa opuestamente incrementando un 19% el número de escuchas los días miércoles en comparación con las 5,700 escuchas promedio en lunes y viernes.
# Sin embargo, sería necesario conocer las fechas para saber si esta evaluacion comprende un rango de varias semanas y determinar si dicho comportamiento se repite y las magnitudes en que lo hace. Dicho de otro modo, el presente estudio no ayuda para asumir que cada semana es igual.

# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Muy buena conclusión! Sin duda hace falta más información. Pero, por lo que podemos ver aquí, la hipótesis se aceptaría ya que, como comentas, exisste efectivamente una diferencia.
# 
# </div>

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# <div class="alert alert-block alert-success"> 
# <b>Comentario del Revisor #1</b> <a class="tocSkip"></a>
# 
# Excelente trabajo Oscar! Felicidades
# 
# </div>

# [Volver a Contenidos](#back)
