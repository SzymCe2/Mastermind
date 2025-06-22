import unittest
import random
from  unittest import  mock
from generator_kodu import KodGenerator
from porownywanie_odp import porownywanie_odp


class Test_Generator(unittest.TestCase):
    def setUp(self):
        self.generator=KodGenerator()

    def test_latwe(self):
        kod = self.generator.generuj_kod(trudnosc='latwy')
        self.assertEqual(len(kod),4)
        kolory_podst = ['czerwony', 'zielony', 'niebieski', 'żółty', 'biały', 'czarny']
        for elem in kod:    
            self.assertIn(elem, kolory_podst)
    
    def test_srednie(self):
        kod = self.generator.generuj_kod(trudnosc='sredni')
        self.assertEqual(len(kod),6)
        kolory_podst = ['czerwony', 'zielony', 'niebieski', 'żółty', 'biały', 'czarny']
        for elem in kod:    
            self.assertIn(elem,kolory_podst)

    def test_trudny(self):
        kod = self.generator.generuj_kod(trudnosc ='trudny')
        self.assertEqual(len(kod),8)
        kolory_rozsz = ['czerwony', 'zielony', 'niebieski', 'żółty', 'fioletowy', 'pomarańczowy', 'biały', 'czarny']
        for elem in kod:
            self.assertIn(elem, kolory_rozsz)

    #def test_unikalne_true(self):
     #   with mock.patch('random.sample', kolory_podst = ['czerwony', 'zielony', 'niebieski', 'żółty','biały', 'czarny'] ):
      #      kod = self.generator.generuj_kod(4, True,'kolory', )
       #     self.assertEqual(len(kod),4)
        #    self.assertEqual(len(set(kod)),len(kod))
         #   self.assertEqual(kod, kolory_podst)

    def test_len_higher(self):
        kod = self.generator.generuj_kod(dlugosc=7, unikalne=True, tryb='kolory')
        self.assertEqual(kod, [])

    def test_zly_tryb(self):
        kod= self.generator.generuj_kod(tryb = 'kolory_teczy')
        self.assertEqual(kod, [])

    def test_liczby_podstawowe(self):

        kod = self.generator.generuj_kod(tryb='liczby')
        self.assertEqual(len(kod), 4)
        liczby_podst = ['1', '2', '3', '4', '5', '6']
        for elem in kod:
            self.assertIn(elem, liczby_podst)

    def test_liczby_rozszerzone(self):
        kod = self.generator.generuj_kod(tryb='liczby_roz')
        self.assertEqual(len(kod), 4) # Domyślna długość to 4 jeśli nie podano inaczej
        liczby_rozsz = ['1', '2', '3', '4', '5', '6', '7', '8']
        for elem in kod:
            self.assertIn(elem, liczby_rozsz)
    

class Test_Porownywanie(unittest.TestCase):
    def setUp(self):
        kod = ['żółty', 'czerwony', 'zielony', 'niebieski']
        self.comparison=porownywanie_odp(kod)


    def test_dlugosc_odp(self):
        too_long = ['czerwony', 'żółty', 'niebieski', 'zielony', 'czarny']
        with self.assertRaises(ValueError):
            self.comparison.porownanie(too_long)
        too_short = ['czerwony', 'żółty']
        with self.assertRaises(ValueError):
            self.comparison.porownanie(too_short)
    
    def test_zliczanie_trafien(self):
        player = ['żółty', 'niebieski', 'zielony', 'czerwony']
        self.assertEqual(self.comparison.porownanie(player), (2,1))
