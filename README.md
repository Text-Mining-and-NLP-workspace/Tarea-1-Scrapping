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
## Descripcion:
Webscrapper de reseñas y calificaciones del top 25 de peliculas mas popular en el sitio <a href="https://www.imdb.com/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/245px-IMDB_Logo_2016.svg.png" width="46" height="24"/></a>
 
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

Most popular
<br/>
<img src="https://drive.google.com/file/d/1HKGSvlOFZjAfsHoJ5edDwWr5k2aMjG2y/view?usp=drivesdk"/>
<br/>
users reviews
<br/>
<img src="https://drive.google.com/file/d/1Hxj80PlWPUxIo0ipq92dsbF_0AONMbP_/view?usp=drivesdk"/>
<br/>
load more
<br/>
<img src="https://drive.google.com/file/d/10Eof7nIJhiLLPq2U2xwz358fubsh22H0/view?usp=drivesdk"/>
<br/>
ajax
<br/>
<img src="https://drive.google.com/file/d/1XjApVoqcZA81ICjbSvewgPII4TQ_zsOx/view?usp=drivesdk"/>
<br/>
datakey
<br/>
<img src="https://drive.google.com/file/d/1dvOjK_GYEx21031A6Zhw8YZ_3x3K-l97/view?usp=drivesdk"/>
<br/>