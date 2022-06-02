<a href="https://www.uvg.edu.gt/"><img style="float: left;" src="https://www.uvg.edu.gt/wp-content/uploads/socialshare-logo.jpg" width="90" height="90"></a>
**_Coorporate Master in Applied Data Science_**<br/>
**_Text Mining & Natural Language Processing_**<br/>
**_Catedratico: Pedro Alberto Aguilar Nuñez_**<br/>
<br/>

Integrantes:
- Aldo Montenegro Margnoni
- Gabriel Fernando Montenero Ortiz
- Axel Adolfo Muralles Carranza

# Tarea 1 Scrapping 
#### Descripcion:
Webscrapper de reseñas y calificaciones del top 25 de peliculas mas popular en el sitio IMDb<a href="https://www.imdb.com/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/245px-IMDB_Logo_2016.svg.png" width="115" height="58"/></a>
 
#### Requerimientos:
- Requiere instalacion de [Anaconda Distribution](https://www.anaconda.com/products/distribution) o [miniconda](https://docs.conda.io/en/latest/miniconda.html)

#### Instrucciones:

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

#### Estructura del archivo de salida

El archivo de salida tiene formato **csv**, y consta de dos columnas
- **rating:** la calificacion de la reseña, en numeros enteros del 1 al 10
- **review:** el texto completo de la reseña del usuario
<br/>
 
| rating | review|
|-----------|:-----------:|
| 10 | "What a great movie" |
| 5 | "Good CGI, but that's a given nowadays"|
| 1 | "Don't watch this movie" |

#### Descripcion del Contenido del sitio Web




