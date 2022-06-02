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
<img src="https://lh3.googleusercontent.com/vIqMjE6VFqM_L-R4GDUjF7C7B9ayDM-pjk8KqoQ17DWtxsi8fTy3Pov_zONhrxmoySmVi5qAeFbelJFIzt7-hPFTe-UBOhr_XW26zUyS6r_39Bn7Frtn71UL3HSbrjj0Ney8zYeeNw=w2400"/>
<br/>
users reviews
<br/>
<img src="https://lh3.googleusercontent.com/Ok3RKu91eZrp9bafJjKnpYhZDx6gRaSIwYEmqLTsejVNNU_c9WmdPmc0ozFwiX8muQD5c5GRt5t1GFX8SbRmv0OEek7X_JF3SSzfFREanpO5j3oURmpH2qBCBCUZwrqjUyEGYrCWdw=w2400"/>
<br/>
load more
<br/>
<img src="https://lh3.googleusercontent.com/9bxwbTn-vzKTjoWS09DeQ7mGiNoNpc3AMbzQJf5pbXj6NfI80z6g6mvQzLypHVfMgJKMf6otCRyyKWId9qOYbF5Xum0aP4wP_xJJQlM_090_YRkK60UncGScQLZkxS3A9IjGydprxg=w2400"/>
<br/>
ajax
<br/>
<img src="https://lh3.googleusercontent.com/_PrdNcOCpixmLoBtzCCNwEmex96I5VhOPnyDZm-XIfTrrojnmRTPOxvmWwq5YLQGKe4Qwt-zgtBCpF4B42PXU3Yky_uDx-dyUaN49UyTKYfZzWkbs3CLvFXSlMsNNl_Lbb8v7tC0Yg=w2400"/>
<br/>
datakey
<br/>
<img src="https://lh3.googleusercontent.com/y-DRyI0_XGJ90dlXde1av-YalNvykbxUO32V4cEkrlzd-niaahcRdqqmF6j-0CIIVRmRFWVfZdmSB4wky314LifENcj-n4xnSdguAGiZRF3KX8xUyGEBEtKvCEtf2S1TvJikZZtAew=w2400"/>
<br/>