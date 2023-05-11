import unittest
from CanIBuyBeer import canIBuyBeer

class TestCanIBuyBeer(unittest.TestCase):
    
    def test_valid_age_krogen_promilleHalt_under_limit(self):
        self.assertTrue(canIBuyBeer(18, "K", 0.5))
    
    def test_valid_age_systemet_promilleHalt_under_limit(self):
        self.assertTrue(canIBuyBeer(20, "S", 0.2))
    
    def test_invalid_age_krogen_promilleHalt_over_limit(self):
        self.assertFalse(canIBuyBeer(17, "K", 1.2))
    
    def test_invalid_age_systemet_promilleHalt_over_limit(self):
        self.assertFalse(canIBuyBeer(21, "S", 1.1))
    
    def test_invalid_age_krogen_promilleHalt_under_limit(self):
        self.assertFalse(canIBuyBeer(17, "K", 0.3))
    
    def test_invalid_age_systemet_promilleHalt_under_limit(self):
        self.assertFalse(canIBuyBeer(20, "S", 0.9))
    
    def test_invalid_location(self):
        with self.assertRaises(ValueError):
            canIBuyBeer(18, "X", 0.5)

if __name__ == '__main__':
    unittest.main()