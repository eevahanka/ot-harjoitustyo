# Testausdokumentti

Ohjelmaa on testattu sekä manuaalisesti, että automatisoiduin testein.

## Sovelluslogiikan testaus

Square- ja Game-luokista koostuvaa sovelluslogiikkaa testataan  TestSquare- sekä TestGame-luokilla.

## Testauskattavuus

Käyttöliittymää lukuunottamatta testauksen haaraumakattavuus on 71%

![kuva haaraumakattavuudesta](/dokumentaatio/photos/haaraumakattavuus.jpg)

Testaamatta jäi repositorio sekä importerroriin varautuneet try-except:n käyttö importatessa.

## Järjestelmä testaus

Sovellusta on testattu [käyttöhjeen](/dokumentaatio/kayttoohje.md) ohjeilla, macOS ja Linux käyttöjärjestelmillä. 
[Vaatimusmäärittelyn](/dokumentaatio/vaatimusmaarittely.md) mukaiset toiminnallisuudet on testattu toimiviksi.

## Laatuongelmat

Sovellus ei anna virheilmoitusta mikäli tietokantaa ei ole alustettu ennen sovelluksen avausta.
