# Minesweeper

## todo

- arkkitehtuurin kuvat
- poista beta sovelluksen otsikosta 
- käyttöohje
- testausdokumentti 


## Dokumentaatio

- [vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)
- [arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)
- [käyttöohje](/dokumentaatio/kayttoohje.md)

## Komennot

- Asenna riippuvuudet komennolla: 

````          poetry install````

- Luo database ennen sovelluksen käynnistämistä:

````  poetry run invoke build````

- Käynnistä sovellus komennolla:

````  poetry run invoke start````

- Käynnistä testit komennolla:

````  poetry run invoke test````

- Luo testikattavuusraportti komennolla:

````  poetry run invoke coverage-report````

- pylint raportti komennolla:

````  poetry run invoke lint````
