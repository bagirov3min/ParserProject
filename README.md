# Парсер валюты и списка лучших фильмов

## Описание проекта

Этот проект представляет собой инструмент для парсинга данных о курсе валюты и списке 100 лучших фильмов с веб-сайтов. Он включает в себя следующие компоненты:

### Парсинг списка 100 лучших фильмов

1. Открытие страницы [AFI's 100 Years...100 Movies](https://www.afi.com/afis-100-years-100-movies/).
2. Извлечение списка фильмов.
3. Вывод списка фильмов в терминал по одному на строке.

### Парсинг курса рубля к доллару

1. Открытие страницы [mfd.ru/currency/?currency=USD](http://mfd.ru/currency/?currency=USD).
2. Извлечение таблицы с данными о курсе рубля к доллару.
3. Вывод последних 40 дат, курса рубля к доллару и изменения цены в терминал.

### Построение графика курса рубля к доллару

1. Открытие страницы [mfd.ru/currency/?currency=USD](http://mfd.ru/currency/?currency=USD).
2. Извлечение таблицы с данными о курсе рубля к доллару.
3. Построение графика изменения курса рубля к доллару за последние 40 дней.

## Инструкции по запуску

Чтобы запустить парсинг и просмотр результатов, выполните следующие действия:

1. Установите зависимости из файла `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   
2. Для парсинга списка фильмов выполните:
    ```bash
    python parser_films.py

3. Для парсинга курса рубля и вывода данных в терминал:
    ```bash
    python parser_usd_cli.py

4. Для построения графика курса рубля выполните:
    ```bash
    python parser_usd_plotlib.py

## Примеры результатов

## Парсинг списка 100 лучших фильмов:
1. Citizen Kane (1941)
2. Casablanca (1942)
3. The Godfather (1972)
...

## Парсинг курса рубля:

Дата        Курс рубля к доллару  Изменение
20.07.2023  91.2046               +0.514
21.07.2023  90.8545               −0.3501
22.07.2023  90.3846               −0.4699

График курса рубля:

[График курса рубля](image%2Ffigure.png)