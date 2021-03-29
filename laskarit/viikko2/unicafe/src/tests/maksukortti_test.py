import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    
#Rahan lataaminen kasvattaa saldoa oikein
    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
#Rahan ottaminen toimii
    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
#Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_saldo_vähenee_oikein_kun_tarpeeksi_rahaa(self):
        self.maksukortti.lataa_rahaa(990)
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
#Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
#Metodi palauttaa True, jos rahat riittivät ja muuten False
    def test_metodi_palauttaa_true_kun_raha_riittää(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(self.maksukortti.ota_rahaa(900), True)
    def test_metodi_palauttaa_false_kun_ei_rahaa_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(900), False)
