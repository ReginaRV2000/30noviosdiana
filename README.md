#README
# 30 Novios de Diana
### Proyecto hecho por Regina, Diana, Gisele, y Giovanni 

### IMPORTANTE para poder usarlo y que salgan las imagenes hay que correr aunque sea la primer parte del archivo 30 Novios de Diana. Para correr la app se necesitan las siguientes librerias: 
- streamlit, pandas, streamlit_extras.

## Instalación y Uso

1. Clonar este repositorio o descargar los archivos.

   ```bash
   git clone https://github.com/ReginaRV2000/30noviosdiana.git
   cd 30-novios-de-diana
   ```

2. Instalar las dependencias necesarias.

   ```bash
   pip install -r requirements.txt
   ```
   o
   ```bash
   pip install streamlit
   pip install pandas
   pip install streamlit_extras
   ```

4. Ejecutar la aplicación.

5. Interactuar con la aplicación y descubrir quién es el mejor candidato

   ```bash
   streamlit run compatibilidad_app.py

Este proyecto emplea técnicas de web scraping y una API de compatibilidad amorosa para generar un archivo CSV que evalúa los niveles de compatibilidad de Diana con diversos actores famosos. Posteriormente, se utiliza Streamlit para desarrollar una aplicación interactiva que permite seleccionar a los "novios" y visualizar su compatibilidad.

## Contenido de la Carpeta

### 1. Archivos de Datos y Procesamiento

#### 30 Novios de Diana.ipynb
- Contiene el proceso de generación del CSV utilizando web scraping y la Love Compatibility Calculator API - APIVerve.
- El web scraping se realiza desde la siguiente fuente:
  - "OkChicas - Actores menores de 45 guapos"
- Es posible modificar el nombre de Diana por otro para generar una nueva compatibilidad.
- Archivo de salida generado: `compatibilidad_diana2.csv` (incluido en la carpeta, no es necesario ejecutarlo nuevamente).

#### 30novios.ipynb
- Documento en formato Markdown que proporciona una documentación detallada del proceso.
- Incluye los errores encontrados y las soluciones implementadas.

### 2. Aplicación Interactiva

#### compatibilidad_app.py
- Aplicación desarrollada con Streamlit.
- Permite seleccionar actores mediante casillas de verificación (checkboxes) y muestra la compatibilidad con Diana (o cualquier nombre utilizado en el CSV).
- Características:
  - Visualización de emojis en función del nivel de compatibilidad.
  - Mensajes personalizados que varían según el porcentaje de compatibilidad.
  - Reproducción de sonidos temáticos al seleccionar cada actor.
  - Imágenes dinámicas que aumentan de tamaño al seleccionar un actor.

### 3. Archivos de Sonido

Los archivos de sonido reflejan la compatibilidad obtenida:

- `church.mp3` → Compatibilidad ≥ 95
- `applause.mp3` → Compatibilidad 90 - 94
- `aww.mp3` → Compatibilidad 86 - 89
- `cricket.mp3` → Compatibilidad 81 - 85
- `boo.mp3` → Compatibilidad 71 - 80
- `fail.mp3` → Compatibilidad < 70

### 4. Otros Archivos

#### requirements.txt
- Contiene las dependencias necesarias para la ejecución del proyecto.


## Requisitos

- Python 3.8 o superior
- Librerías necesarias: pandas, streamlit, requests, beautifulsoup4, streamlit-extras

## Notas

- Para modificar el nombre de Diana, es necesario ejecutar `30 Novios de Diana.ipynb` y generar un nuevo archivo `compatibilidad_diana2.csv`.
- Si los sonidos no se reproducen, se recomienda verificar la configuración de audio del navegador.
- Si las imagenes no aparecen hay que correr el archivo 30 Novios de Diana
