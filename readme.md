# Projekt ASEID 2021

### Zadanie 2, podpunkt C

# Cel projektu
Celem projektu jest dokonanie analizy danych zawierających informacje na temat poruszających się taksówek w Nowym Jorku (yellow and green taxi). Zbiór danych zawiera następujące informacje (pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts).

# Wymagania
* Python version > 3.8
* Java version > 8

```python
 pip3 install -r requirements.txt
 ```

## Java
PySpark wymaga Javy do uruchamiania skryptów. Konieczne jest wcześniejsze pobranie jre i jdk, oraz ustawienie zmiennej środowiskowej do Javy .

# Wykonanie
Wszystkie założenia projektowe zostały spełnione, program został uruchomiony za pomocą putty na serwerach AWS, a także lokalnie. Wyliczona została średnia prędkość taksówki na podstawie informacji na temat czasu (pick-up and drop-off dates/times) oraz przebytej odległości (trip distances). Przeanalizowane dane pochodzą z okresu maj 2019 - maj 2020.

![obraz](https://user-images.githubusercontent.com/51135031/134080645-3ad89005-f037-4f2e-8c81-ec4c0189bc5c.png)

Z powodu ogromnej ilości danych do pobrania i uruchomienia projekt został uruchomiony w całości jedynie poprzez serwer, a lokalnie uruchamiane były wersje z mocno okrojoną liczbą danych.

# Zastosowane rozwiązania w kodzie
Dane do obróbki pochodzą z oficjalnej rządowej strony (https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Wczytywane pliki csv są zamieniane na wektory zawierające dane, a następnie liczone są średnie prędkości. Podczas przetwarzania danych zauważyliśmy anomalie w postaci przebytych nieosiągalnie dużych odległości, zbyt długich czasów jazdy, czy zbyt wysokich prędkości na trasie. Zdecydowaliśmy się na obcięcie odstających wartości, aby otrzymane średnie były wierną reprezentacją faktycznych wartości.
Zastosowane w naszym kodzie biblioteki to:
* numpy - standardowa biblioteka Pythona, służąca do poprawienia szybkości obliczeń
* matplotlib - biblioteka używana do tworzenia wizualnej reprezentacji danych w postaci wykresu i zapisywania go w klastrze obliczeniowym
* pyspark, boto3 - używane do łączenia się z serwerami aws

# Wyniki
Otrzymane wyniki są w granicach rozsądku i wydają się być dobrą reprezentacją ruchu taksówek w Nowym Jorku. Na wykresie widać, że średnia prędkość zielonych taksówek jest każdego miesiąca wyższa niż taksówek zielonych. Ciekawym zjawiskiem jest skokowy wzrost prędkości na przełomie marca i kwietnia 2020 roku. Podejrzewamy, że ma on związek z obostrzeniami przemieszczania się, wprowadzonymi w tamtym okresie.

![obraz](https://user-images.githubusercontent.com/51135031/134083068-5c1f7bcb-ff51-4f9a-b2a0-90d2524984d1.png)

Wykres przedstawia średnią szybkość zielonych i żółtych taksówek w przeciągu danego miesiąca w przedziale maj 2019- maj 2020

## Skład Grupy
* Barbara Klaudel
* Michał Dramiński
* Sebastian Krajna
