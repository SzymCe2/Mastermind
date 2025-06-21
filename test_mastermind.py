import unittest
import random

class Test_Generator(unittest.TestCase):
    def setUp(self):
        self.generator=KodGenerator()

    def test_latwe(self):
        kod = self.generator.generuj_kod(trudnosc=='latwy')
        self.assertEqual(len(kod),6)
        self.assertEqual(len(set(kod)),len(kod))
        kolory_podst = ['czerwony', 'zielony', 'niebieski', 'żółty']
        for elem in kod:    
            self.assertIn(element, kolory_podst)
    
    def test_srednie(self):
        kod = self.generator.generuj_kod(trudnosc=='sredni')
        self.assertEqual(len(kod),6)
        kolory_podst = ['czerwony', 'zielony', 'niebieski', 'żółty']
        for elem in kod:    
            self.assertIn(elem,kolory_podst)
    def test_trudny(self):
        kod = self.generator.generuj_kod(trudnosc =='trudny')
        self.assertEqual(len(kod),8)
        kolory_rozsz = ['czerwony', 'zielony', 'niebieski', 'żółty', 'fiolotowy', 'pomarańczowy']
        for elem in kod:
            self.assertIn(elem, kolory_rozsz)
    def test_unikalne_true(self):
        with mock.patch('random.sample', kolory_podst = ['czerwony', 'zielony', 'niebieski', 'żółty'] ):
            kod = self.generator.generuj_kod(unikalne == True)
            self.assertEqual(len(kod),4)
            self.assertEqual(len(set(kod)),len(kod))
            self.assertEqual(kod, kolory_podst)
    def test_len_higher(self):
        kod = self.generator.generuj_kod(dlugosc=7, unikalne=True, tryb='kolory')
        self.assertEqual(kod, [])
    def test_zly_tryb(self):
        kod= self.generator.generuj_kod(tryb == 'kolory_teczy')
        self.assertEqual(kod, [])
    
    
        

        