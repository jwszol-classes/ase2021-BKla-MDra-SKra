# Projekt ASE 2021

## Temat zadania: 

### Zadanie 2
Dokonaj analizy danych zawierających informacje na temat poruszających się taksówek w Nowym Jorku (yellow and green taxi). Zbiór danych zawiera następujące informacje (pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts). 

Zadanie wymaga przeanalizowania danych w następującym przedziale czasowym:
* Rok 2020 / Maj
* Rok 2019 / Maj

Wykryj anomalie pomiędzy (pick-up and drop-off dates/times) a przebytym dystansem. Z wykorzystaniem metody grupowania według k-średnich znajdź i zinterpretuj wyniki.
Skoreluj informacje dotyczące typu płatności a ilości przewożonych pasażerów
Wylicz średnią prędkość taksówki na podstawie informacji na temat czasu (pick-up and drop-off dates/times) oraz przebytej odległości (trip distances)

# Kroki

## Spark
Instalacja sparka https://phoenixnap.com/kb/install-spark-on-windows-10
## EC2
Aby mieć bezpieczny dostęp do utworzonego przez nas później klastra, musimy utworzyć klucz. W konsoli, w 'AWS services' przechodzimy do EC2 -> Key Pairs -> Create Key Pair -> Nadajemy nazwę -> wybieramy Putty -> Zapisujemy.
## EMR
Po zalogowaniu się do konsoli, wybieramy z 'AWS services' EMR i tworzymy cluster wybierając w software configuration Spark, w 'Hardware configuration' wybieramy m4.xlarge a na samym dole wybieramy klucz, który wcześniej utworzyliśmy. Tworzymy klaster.
Po wyskoczeniu nowego okna szukamy 'Security groups for Master' i przechodzimy do miejsca na które wskazuje. Zaznaczamy nazwę grupy, gdzie w 'description' jest Master. Poniżej przechodzimy do 'Inbound rules' i edytujemy. Na samym dole klikamy 'add rule', w której jako typ ustawiamy ssh i source typ jako anywhere. (Niezalecane dla produkcji, wtedy wybieramy konkretne ip). Zapisujemy zmiany.

## S3 bucket
W konsoli, w 'AWS services' przechodzimy do S3 i tworzymy nowy bucket i uploudujemy do niego nasze pliki ze skryptem.

## Putty
Pobieramy putty oraz puttygen ze strony https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html. Odpalamy PuttyGen i wybieramy wcześniej zapisany przez nas Key Pair i zapisujemy go do ThisPc/Documents/aws/keys. Przechodzimy do wcześniej przez nas utworzonego clustra i znajdujemy 'Master public DNS', wchodzimy w 'Connect to the Master Node Using SSH' i kopiujemy host name field. Odpalamy PuTTy i w miejscu host name wklejamy poprzednio skopiowaną wartość. Connection typ ustawiamy jako SSH. W kategoriach przechodzimy do SSH -> AUTH -> browse i wybieramy wcześniej zapisany plik przez puttygen. Klikamy open. Wpisujemy '''aws s3 cp s3://<nazwa_bucketa>/<nazwa_pliku.py> . '''. Komenda ls sprawdzamy czy plik zostal pobrany. Następnie plik uruchamiamy komenda '''spark-submit <nazwa_pliku.py>'''


## Skład Grupy
* Barbara Klaudel
* Michał Dramiński
* Sebastian Krajna