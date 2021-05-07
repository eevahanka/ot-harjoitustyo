

# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne:

![kuva pakkauskaaviosta](/dokumentaatio/photos/kaavio.jpg)

(pitääpi tehdä uusi)

Pakkaus ui sisältää käyttöliittymän koodin, pakkaus logic sisältää pelinlogiikasta huolehtivan koodin ja repo sisältää pysyväistallennuksesta vastaavan koodin.

## Käyttöliittymä

Käyttöliittymään kuuluu 3 näkymää:

- Menu
- Peli
- Statistiikka

## Sovelluslogiikka

Pelin toiminta perustuu luokkiin Game ja Square:

![Luokkien Peli ja Saquare suhde](/dokumentaatio/photos/??????.jpeg)

(ei ole olemassa)

Luokka Peli tarjoaa 2 metodia käyttöliittymälle, jotka vastaavat hiiren painallukista pelissä:
- handle_leftclick_on_board
- handle_rightclick_on_board

Luokka Square tarjoaa yhden metodin Pelille, jolla liputetaan ruutu/ poistetaan ruudusta lippu:
- flagging

## Pysyvyväistalletus

Luokka GameRepository vastaa tiedon pysyvyväistalletuksesta SQLite -tietokantaan.
Päättyneet pelit tallennetaan SQLite -tietokannan tauluun ````games````, joka alustetaan initialize_database.py -tiedostossa.

## Päätoiminnallisuudet

### Uuden pelin luominen

Kun käyttäjä klikkaa uusi peli -painiketta luodaan uusi peli.

![sekvenssikaavio uuden pelin luomisesta](/dokumentaatio/photos/????.jpeg)

(ei ole olemassa)

### pelin päättyminen

Kun peli päättyy tallennetaan tieto oliko peli voitto vai häviö, sekä aikaleima tietokantaan

![sekvenssikaavio pelin päättymisestä](/dokumentaatio/photos/????.jpeg)

(ei ole olemassa)

### Vasemman hiirenpainikkeen painaminen

Kun pelissä käyttäjä klikkaa vasemmalla painikkeella, niin avataan klikattu ruutu ja mikäli ko ruutu on pommi, peli päättyy


![sekvenssi kaavio](/dokumentaatio/photos/sekvenssikaavio_????.jpg)

(ei ole olemassa)

### Oikean hiirenpainikkeen painaminen

Kun pelissä käyttäjä klikkaa oikealla painikkeella niin liputetaan klikattu ruutu/ poistetaan klikatusta ruudusta lippu:

![sekvenssi kaavio](/dokumentaatio/photos/sekvenssikaavio_leftclick.jpg)

(typo)






