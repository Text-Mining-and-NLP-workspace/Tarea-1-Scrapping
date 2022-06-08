<a href="https://www.uvg.edu.gt/"><img align="left" src="https://www.uvg.edu.gt/wp-content/uploads/socialshare-logo.jpg" width="90" height="90"></a>
**_Corporate Master in Applied Data Science_**<br/>
**_Text Mining & Natural Language Processing_**<br/>
**_Catedratico: Pedro Alberto Aguilar Nuñez_**<br/>
<br/>

Integrantes:
- Aldo Montenegro Margnoni
- Gabriel Fernando Montenero Ortiz
- Axel Adolfo Muralles Carranza

# Tarea 1 Scrapping 

- [Descripcion](#descripcion)
- [Requerimientos](#requerimientos)
- [Instrucciones](#instrucciones)
- [Estructura del archivo de salida](#estructura-del-archivo-de-salida)
- [Descripcion del contenido del sitio web](#descripcion-del-contenido-del-sitio-web)
- [Contribuciones](#contribuciones)
- [Settings](#settings)


## Descripcion:
Webscrapper de reseñas y calificaciones del top 25 de peliculas mas populares en el sitio <a href="https://www.imdb.com/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/245px-IMDB_Logo_2016.svg.png" width="46" height="24"/></a>
 
## Requerimientos:
- Requiere instalacion de [Anaconda Distribution](https://www.anaconda.com/products/distribution) o [miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Instrucciones:

clonamos este repositorio en el directorio deseado desde una terminal, para windows podemos utilizar [Git Bash](https://gitforwindows.org/) 
```
git clone https://github.com/Text-Mining-and-NLP-workspace/Tarea-1-Scrapping.git
```
Desde la terminal o anaconda prompt (windows) creamis un ambiente virtual con conda (reemplazar my_enviroment con el nombre deseado)
```
conda create -n my_enviroment
```
cuando conda pregunte por la confirmacion responder con _y_
```
proceed ([y]/n)?
```
una vez creado el ambiente virtual, proceder a activarlo
```
conda activate my_enviroment
```
instalamos scrapy en nuestro ambiente
```
conda install scrapy -c conda-forge
```
nos cambiamos hacia el path en donde se clono el repositorio
```
cd Tarea-1-Scrapping/
```
ejecutamos el siguiente comando para ejecutar la spider y comenzar el scrapping
```
scrapy crawl imdb
```
como salida se creara el archivo **_imdb_most_popular_reviews.csv_** en nuestro directorio de trabajo

## Estructura del archivo de salida

El archivo de salida tiene formato **csv**, y consta de dos columnas
- **rating:** la calificacion de la reseña, en numeros enteros del 1 al 10
- **review:** el texto completo de la reseña del usuario
<br/>

| rating | review|
|-----------|:-----------:|
| 10 | "What a great movie" |
| 5 | "Good CGI, but that's a given nowadays"|
| 1 | "Don't watch this movie" |
<br/>
<br/>

## Descripcion del Contenido del sitio Web 
<a href="https://www.imdb.com/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/245px-IMDB_Logo_2016.svg.png"/></a><br/>
> **Internet Movie Database** (IMDb, en español: Base de datos de películas en Internet) es una base de datos en línea que en un principio almacena información relacionada con películas, y con el tiempo se transforma en la base de datos más grande del mundo donde se encuentran programas de televisión, eventos en vivo y difundidos en televisión o en la web, entrega de premios y especiales. Se encuentra el personal de equipo de producción (incluyendo directores y productores), actores, series y programas de televisión, videojuegos, actores de doblaje y personajes ficticios que aparecen en los medios de entretenimiento visual. Recibe más de 100 millones de usuarios únicos al mes y cuenta con una versión móvil. IMDb fue inaugurada el 17 de octubre de 1985, y en 1998 fue adquirida por Amazon.com. _(fuente: Wikipedia)_

El sitio IMDb cuenta con un conteo de las peliculas mas populares entre los usuarios, [IMDb Most Popular](https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm) es aqui donde iniciamos nuestra tarea, raspando la lista de urls para las peliculas mas populares, este ranking cuenta con 100 entradas de las cuales nosotros utilizaremos las primeras 25: 
<br/>
<img src="https://lh3.googleusercontent.com/vIqMjE6VFqM_L-R4GDUjF7C7B9ayDM-pjk8KqoQ17DWtxsi8fTy3Pov_zONhrxmoySmVi5qAeFbelJFIzt7-hPFTe-UBOhr_XW26zUyS6r_39Bn7Frtn71UL3HSbrjj0Ney8zYeeNw=w2400"/>
<br/>

Una vez con el url el cual contiene el ID de la pelicula, podemos ingresar a la pagina donde se encuentran las reseñas de usuarios para cada una de las peliculas en nuestra lista, por ejemplo [https://www.imdb.com/title/**tt1745960**/reviews](https://www.imdb.com/title/tt1745960/reviews), esta es la pagina donde se encuentra la informacion de nuestro interes: 
<br/>
<img src="https://lh3.googleusercontent.com/Ok3RKu91eZrp9bafJjKnpYhZDx6gRaSIwYEmqLTsejVNNU_c9WmdPmc0ozFwiX8muQD5c5GRt5t1GFX8SbRmv0OEek7X_JF3SSzfFREanpO5j3oURmpH2qBCBCUZwrqjUyEGYrCWdw=w2400"/>
<br/>
En esta pagina se observan reseñas de usuarios,donde cada reseña cuenta con una calificacion sobre 10 puntos y un texto con las ideas, pensamientos y conclusiones del usuario acerca de la pelicula de la cual estamos extrayendo la informacion, las reseñas se encuentran paginadas en 25 por pagina y el metodo de paginacion es por medio de un boton "Load More" el cual carga a la pagina otro bloque de 25 reseñas al presionarlo.
<br/>
<img src="https://lh3.googleusercontent.com/9bxwbTn-vzKTjoWS09DeQ7mGiNoNpc3AMbzQJf5pbXj6NfI80z6g6mvQzLypHVfMgJKMf6otCRyyKWId9qOYbF5Xum0aP4wP_xJJQlM_090_YRkK60UncGScQLZkxS3A9IjGydprxg=w2400"/>
<br/>

Utilizando las **Herramientas para desarrolladores** del navegador, podemos observar que al presionar el boton, hace un GET hacia el script Java Asincrono + XML (AJAX) **/_ajax** con parametros **ref_** y **paginationKey**, este ultimo se utiliza para poder obtener la siguiente pagina
<br/>
<img src="https://lh3.googleusercontent.com/_PrdNcOCpixmLoBtzCCNwEmex96I5VhOPnyDZm-XIfTrrojnmRTPOxvmWwq5YLQGKe4Qwt-zgtBCpF4B42PXU3Yky_uDx-dyUaN49UyTKYfZzWkbs3CLvFXSlMsNNl_Lbb8v7tC0Yg=w2400"/>
<br/>
EL valor necesario para el siguiente **paginatioKey** se encuentra dentro del elemento **div** con clase **load-more-data** con atributo **data-key**, y podemos realizar el request hacia la url en el atributo **data-ajaxurl**
<br/>
<img src="https://lh3.googleusercontent.com/y-DRyI0_XGJ90dlXde1av-YalNvykbxUO32V4cEkrlzd-niaahcRdqqmF6j-0CIIVRmRFWVfZdmSB4wky314LifENcj-n4xnSdguAGiZRF3KX8xUyGEBEtKvCEtf2S1TvJikZZtAew=w2400"/>
<br/>
Con estos datos podemos realizar las itereaciones necesarias para obtener todas las reseñas y calificaciones de una pelicula.

## Contribuciones

- Aldo Montenegro Margnoni
    - Analisis de elementos web, y extraccion de selectores
    - Validacion [robots.txt](https://www.imdb.com/robots.txt)
    - Desarrollo Scrapy spider
    - Redaccion README.md
    
<br/>

- Gabriel Fernando Montenero Ortiz
    - Construccion de string FEEDS para generacion de archivo de salida
    - Seleccion de parametros de configuracion de concurrencias settings.py
    - Desarrollo Scrapy spider
    - Redaccion README.md
    
<br/>

- Axel Adolfo Muralles Carranza
    - Analisis e implementacion de Paginacion en Scrapy spider
    - Desarrollo Scrapy spider
    - Formato README.md
    - Creacion repositorio en GitHub

<br/>

- German Antonio Oliva Muralles
    - Desarrollo Scrapy spider
    - Edicion README.md
    - pruebas de ejecucion y calidad
	- validacion de instrucciones

<br/>

## Settings

En el archivo settings.py se agregaron las siguientes configuraciones, debido a que con las concurrencias por defecto causa que el sitio IMDb coloque en lista negra nuestra IP por una cantidad de tiempo, bloqueando asi nuestras peticiones, esto lo hace en general para evitar ataques DoS. las configuraciones causan que la spider tarde mas en obtener toda la informacion, pero se asegura que no se pierdan reseñas y que no se tenga bloqueos por lista negra.

```
USER_AGENT = '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS_PER_DOMAIN = 2

CONCURRENT_REQUESTS_PER_IP = 2
```
