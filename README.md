# Gym Data Project

Bienvenido a Gym Data project, este es un proyecto diseñado para consolidar el aprendizaje y la aplicación de diversas herramientas enfocadas en la ciencia de datos y el desarrollo de software en el área backend.

# Objetivo del Proyecto

Bienvenido a Gym Data un proyecto hecho para adquirir y consolidar conocimientos en ciencia de datos mediante el uso de herramientas como Datasets de Kaggle, Python, Pandas, PostgreSQL, FastAPI entre otros. 

El objetivo de este proyecto es analizar y visualizar datos de una cadena de gimnasios de EEUU, con el fin de obtener valor de las métricas y gráficos hechos sobre el dataset.

## Herramientas y Tecnologías Utilizadas

## Ciencia de Datos

Dataset de Kaggle: De este sitio web se descargaron [datos sobre una cadena de Gimnasios de EEUU.](https://www.kaggle.com/datasets/mexwell/gym-check-ins-and-user-metadata/data?select=users_data.csv). Donde se utilizaron 350.000 filas de datos de archivos .csv.

Pandas: Librería de Python utilizada para la manipulación y limpieza del dataset, facilitando el análisis de grandes volúmenes de datos y la carga de la base de datos en PostgreSQL.

PostgreSQL: Base de datos relacional en la que se almacenan los datos procesados a partir de los archivos CSV, cargados mediante Pandas y gestionados con FastAPI.

## Desarrollo web (Backend)

FastAPI: Framework de Python que se utilizó para construir y desplegar la API, proporcionando un entorno ágil y fácil de usar para el desarrollo de aplicaciones web e implementando la carga de datos desde archivos CSV a PostgreSQL.

## Desarrollo web (Frontend)

React: Framework de JavaScript utilizado para la creación de la interfaz de usuario.

Recharts: Biblioteca de gráficos de Javascript para React, empleada para la visualización de datos mediante componentes para la creación de gráficos.

Axios: Utilizado para la comunicación de la API con el frontend, permitiendo que se puedan mostrar los datos al usuario.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.