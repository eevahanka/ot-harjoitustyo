# Käyttöohje

## Ohjelman käynnistäminen

- Asenna riippuvuudet komennolla: 

````          poetry install````

- Luo database ennen sovelluksen käynnistämistä:

````  poetry run invoke build````

- Käynnistä sovellus komennolla:

````  poetry run invoke start````

## Käyttö

Ohjelman avatessa avautuu näkymä:

![kuva menusta](/dokumentaatio/photos/kuva_menusta.jpg)

Painamalla  _Stats_ avautuu näkymä jossa on pelin statistiikka  ja painamalla _Uusi peli_ avautuu peli näkymä:

![kuva pelistä](/dokumentaatio/photos/kuva_pelista.jpg)

Painamalla ruutua hiiren vasemmalla painikkeella ruutu "avataan" painamalla oikealla painikkeella ruutu liputetaan.
Pelin loputtua peli palaa automaattisesti menuun.
