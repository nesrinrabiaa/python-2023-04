import unittest
from Bankkonto import Bankomat
# att testa funktionerna i Bankomat

class BankomatTest(unittest.TestCase):
    def setUp(self):
        self.bankomat = Bankomat()
        self.bankomat.skapa_konto('123456', 1000)
        self.bankomat.skapa_konto('654321', 500)

    def test_sätt_in(self):
        self.bankomat.sätt_in('123456', 500)
        self.assertEqual(self.bankomat.saldo('123456'), 1500)
        self.bankomat.sätt_in('654321', 100)
        self.assertEqual(self.bankomat.saldo('654321'), 600)

    def test_ta_ut(self):
        self.bankomat.ta_ut('123456', 500)
        self.assertEqual(self.bankomat.saldo('123456'), 500)
        self.bankomat.ta_ut('654321', 200)
        self.assertEqual(self.bankomat.saldo('654321'), 300)

    def test_sätt_in_noll_belopp(self):
        with self.assertRaises(ValueError):
            self.bankomat.s