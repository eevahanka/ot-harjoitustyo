import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(0)
#Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000, lounaita myyty 0)
    def test_luodun_kassapaatteen_raha_maara_oikea(self):
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)
    def test_luodun_kassapaatteen_edullisten_maara_oikea(self):
        self.assertEqual(int(self.kassapaate.edulliset), 0)
    def test_luodun_kassapaatteen_maukkaiden_maara_oikea(self):
        self.assertEqual(int(self.kassapaate.maukkaat), 0)

#Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
    #Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
    def test_syo_edullisesti_kasvattaa_rahamaaraa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100240)
    def test_syo_edullisesti_antaa_oikean_maaran_vaihtorahaa(self):
        self.assertEqual(int(self.kassapaate.syo_edullisesti_kateisella(300)), 60)
    #Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_syo_edullisesti_kasvattaa_edullisten_maaraa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(int(self.kassapaate.edulliset), 1)
    def test_syo_edullisesti_kasvattaa_maukkaiden_maaraa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(int(self.kassapaate.maukkaat), 1)
    #Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta
    def test_syo_edullisesti_ei_muuta_rahan_maaraa_jos_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(30)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)
    def test_syo_edullisesti_palauttaa_rahat_jos_raha_ei_riita(self):
        self.assertEqual(int(self.kassapaate.syo_edullisesti_kateisella(30)), 30)
    def test_syo_edullisesti_ei_muuta_edullisten_maaraa_jos_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(30)
        self.assertEqual(int(self.kassapaate.edulliset), 0) 
    #maukas
    def test_syo_maukkaasti_ei_muuta_rahan_maaraa_jos_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(30)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)
    def test_syo_maukkaasti_palauttaa_rahat_jos_raha_ei_riita(self):
        self.assertEqual(int(self.kassapaate.syo_maukkaasti_kateisella(30)), 30)
    def test_syo_edullisesti_ei_muuta_maukkaiden_maaraa_jos_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(30)
        self.assertEqual(int(self.kassapaate.maukkaat), 0) 
#seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan oikein
#Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    #Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
    def test_jos_kortilla_rahaa_syo_edullisesti_palauttaa_true(self):
        self.maksukortti.lataa_rahaa(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    def test_jos_kortilla_rahaa_syo_edullisesti_laskee_kortin_saldoa(self):
        self.maksukortti.lataa_rahaa(240)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    #Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    def test_jos_kortilla_rahaa_syo_edullisesti_kasvattaa_edullisten_maaraa(self):
        self.maksukortti.lataa_rahaa(240)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(int(self.kassapaate.edulliset), 1)
    #maukas
    def test_jos_kortilla_rahaa_syo_maukkaasti_palauttaa_true(self):
        self.maksukortti.lataa_rahaa(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_jos_kortilla_rahaa_syo_maukkaasti_laskee_kortin_saldoa(self):
        self.maksukortti.lataa_rahaa(400)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_jos_kortilla_rahaa_syo_maukkaasti_kasvattaa_edullisten_maaraa(self):
        self.maksukortti.lataa_rahaa(400)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(int(self.kassapaate.maukkaat), 1)
    #Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
    def test_jos_ei_rahaa_syo_edullisesti_palauttaa_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
    def test_jos_ei_rahaa_syo_edullisesti_ei_muuta_kortin_saldoa(self):
        self.maksukortti.lataa_rahaa(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
    def test_jos_kortilla_ei_rahaa_syo_edullisesti_ei_muuta_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(int(self.kassapaate.edulliset), 0)
    #maukkaat
    def test_jos_ei_rahaa_syo_maukkaasti_palauttaa_false(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
    def test_jos_ei_rahaa_syo_maukkaasti_ei_muuta_kortin_saldoa(self):
        self.maksukortti.lataa_rahaa(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
    def test_jos_kortilla_ei_rahaa_syo_maukkaasti_ei_muuta_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(int(self.kassapaate.maukkaat), 0)
    #Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    def test_kassan_saldo_ei_muutu_kun_syo_edullisesti_kortilla(self):
        self.maksukortti.lataa_rahaa(400)
        self.kassapaate.syo_edullisesti_kortilla
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)
    def test_kassan_saldo_ei_muutu_kun_syo_maukkaasti_kortilla(self):
        self.maksukortti.lataa_rahaa(400)
        self.kassapaate.syo_maukkaasti_kortilla
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)

#Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_kortin_saldo_kasvaa_oikein_kun_ladataan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 300)
        self.assertEqual(str(self.maksukortti), "saldo: 3.0")
    def test_kassan_saldo_nousee_oikein_kun_ladataan_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 300)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100300)
    def test_jos_ladataan_neg_summa_niin_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 300)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -30)
        self.assertEqual(str(self.maksukortti), "saldo: 3.0")
    def test_jos_ladataan_neg_summa_kassan_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -300)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)