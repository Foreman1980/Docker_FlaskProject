# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask

Данные:
Blood Transfusion Service Center Data Set (https://archive.ics.uci.edu/ml/datasets/Blood+Transfusion+Service+Center)

Data Set Information:

To demonstrate the RFMTC marketing model (a modified version of RFM), this study 
adopted the donor database of Blood Transfusion Service Center in Hsin-Chu City 
in Taiwan. The center passes their blood transfusion service bus to one 
university in Hsin-Chu City to gather blood donated about every three months. To 
build a FRMTC model, we selected 748 donors at random from the donor database. 
These 748 donor data, each one included R (Recency - months since last 
donation), F (Frequency - total number of donation), M (Monetary - total blood 
donated in c.c.), T (Time - months since first donation), and a binary variable 
representing whether he/she donated blood in March 2007 (1 stand for donating 
blood; 0 stands for not donating blood).

Attribute Information:

Given is the variable name, variable type, the measurement unit and a brief 
description. The "Blood Transfusion Service Center" is a classification problem. 
The order of this listing corresponds to the order of numerals along the rows of 
the database.

 - R (Recency - months since last donation)
 - F (Frequency - total number of donation)
 - M (Monetary - total blood donated in c.c.)
 - T (Time - months since first donation)
 - a binary variable representing whether he/she donated blood in March 2007 (1 
stand for donating blood; 0 stands for not donating blood).

Предобработка данных:
Удаление дублирующихся строк, признака "Monetary" как линейно зависящего от признака "Frequency", масштабирование
значений признаков.

(jupyter-notebook - https://github.com/Foreman1980/4.1_MachineLearningInBusiness/blob/Lesson_9/9%20урок/HW9_model-fit-save.ipynb)

Модель: logreg

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/Foreman1980/Docker_FlaskProject.git
$ cd Docker_FlaskProject
$ docker build -t docker-flask .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models>
нужно заменить на полный путь к этому каталогу)
```
$ docker run -d --rm -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/usr/src/app/models docker-flask
```
 - ключ "-d" - запуск контейнера в фоне
 - ключ "--rm" - автоматическое удаление контейнера после остановки
 - ключ "-p" - привязка портов локальной машины и контейнера
 - ключ "-v" - привязка локальной директории и рабочей директории контейнера

### Переходим на localhost:8181


