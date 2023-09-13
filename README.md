# Currency and Top Movies Parser

[English](README.md) | [Русский](README-ru.md)

## Project Description

This project is a tool for parsing data on currency exchange rates and the list of the top 100 movies from websites. It includes the following components:

### Parsing the Top 100 Movies List

1. Open the [Top 100 Movies](https://www.afi.com/afis-100-years-100-movies/) page.
2. Extract the list of movies.
3. Display the list of movies in the terminal, one per line.

### Parsing the Ruble-to-Dollar Exchange Rate

1. Open the [Currency Rates](http://mfd.ru/currency/?currency=USD) page.
2. Extract the table with data on the ruble-to-dollar exchange rate.
3. Display the last 40 dates, ruble-to-dollar exchange rate, and price changes in the terminal.

### Creating a Graph of the Ruble-to-Dollar Exchange Rate

1. Open the [Currency Rates](http://mfd.ru/currency/?currency=USD) page.
2. Extract the table with data on the ruble-to-dollar exchange rate.
3. Create a graph depicting the ruble-to-dollar exchange rate changes over the last 40 days.

## Instructions for Running

To run the parsing and view the results, follow these steps:

1. Install the dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   
2. To parse the list of movies, execute:
    ```bash
    python parser_films.py

3. For parsing the ruble-to-dollar exchange rate and displaying data in the terminal:
    ```bash
    python parser_usd_cli.py

4. To create a graph of the ruble-to-dollar exchange rate, execute:
    ```bash
    python parser_usd_plotlib.py

## Sample Results

## Parsing the Top 100 Movies List:
1. Citizen Kane (1941)
2. Casablanca (1942)
3. The Godfather (1972)
...

Parsing the Ruble-to-Dollar Exchange Rate:

Дата        Курс рубля к доллару  Изменение
20.07.2023  91.2046               +0.514
21.07.2023  90.8545               −0.3501
22.07.2023  90.3846               −0.4699

Exchange Rate Graph:

[Exchange Rate Graph](image%2Ffigure.png)