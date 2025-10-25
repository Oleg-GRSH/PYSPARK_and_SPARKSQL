# Запуск Spark из Docker

## Предварительные требования

Установленный Docker.

## Установка Spark

Будем использовать образ [Jupyter notebooks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) с установленным Apache Spark.

Запускаем контейнер в интерактивном режиме:

```bash
docker run -it -p 8888:8888 -p 4040:4040 -v $(pwd):/home/jovyan/work jupyter/pyspark-notebook
```

Моя обработанная команда для Windows
```bash
docker run -it -p 8888:8888 -p 4040:4040 -v D:/Testing_Spark/PYSPARK_and_SPARKSQL/getting-started-with-pyspark-ru:/home/jovyan/work jupyter/pyspark-notebook
```
Остановка контейнера по CTRL + C.
