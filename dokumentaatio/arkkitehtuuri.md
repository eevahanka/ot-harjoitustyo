

# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne:

![kuva pakkauskaaviosta](/dokumentaatio/photos/kaavio.jpg)


Pakkaus ui sisältää käyttöliittymän koodin, pakkaus logic sisältää pelinlogiikasta huolehtivan koodin ja repo sisältää pysyväistallennuksesta vastaavan koodin.

## Käyttöliittymä

Käyttöliittymään kuuluu 3 näkymää:

- Menu
- Peli
- Statistiikka

## Sovelluslogiikka

Pelin toiminta perustuu luokkiin Game ja Square:

![Luokkien Peli ja Saquare suhde](/dokumentaatio/photos/game_square_suhde.jpg)


Luokka Peli tarjoaa 2 metodia käyttöliittymälle, jotka vastaavat hiiren painallukista pelissä:
- handle_leftclick_on_board
- handle_rightclick_on_board

Luokka Square tarjoaa yhden metodin Pelille, jolla liputetaan ruutu/ poistetaan ruudusta lippu:
- flagging

## Pysyvyväistalletus

Luokka GameRepository vastaa tiedon pysyvyväistalletuksesta SQLite -tietokantaan.
Päättyneet pelit tallennetaan SQLite -tietokannan tauluun ````games````, joka alustetaan initialize_database.py -tiedostossa.

## Päätoiminnallisuudet

### pelin päättyminen

Kun peli päättyy tallennetaan tieto oliko peli voitto vai häviö, sekä aikaleima tietokantaan

![sekvenssikaavio pelin päättymisestä](/dokumentaatio/photos/pelin_tallennus.jpg)

### Vasemman hiirenpainikkeen painaminen

Kun pelissä käyttäjä klikkaa vasemmalla painikkeella, niin avataan klikattu ruutu ja mikäli ko ruutu on pommi, peli päättyy


![sekvenssi kaavio](/dokumentaatio/photos/handle_leftclick.jpg)


### Oikean hiirenpainikkeen painaminen

Kun pelissä käyttäjä klikkaa oikealla painikkeella niin liputetaan klikattu ruutu/ poistetaan klikatusta ruudusta lippu:

![sekvenssi kaavio](/dokumentaatio/photos/handle_rightclick.jpg)
