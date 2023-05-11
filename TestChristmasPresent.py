import unittest

from  ChristmasPresent import ChristmasPresent , p
class TestChristmasPresent(unittest.TestCase):

    def test_christmas_present(self):
        present = ChristmasPresent ("Toy car", 10.5)
        self.assertEqual(present.Name, "Toy car")
        self.assertEqual(present.Price, 10.5)

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person("John")

    def test_add_present(self):
        present1 = ChristmasPresent("Toy car", 10.5)
        present2 = ChristmasPresent("Doll", 15.2)
        self.person.AddPresent(present1)
        self.person.AddPresent(present2)
        self.assertEqual(len(self.person.Presenter), 2)
        self.assertEqual(self.person.Presenter[0], present1)
        self.assertEqual(self.person.Presenter[1], present2)

    def test_get_total(self):
        present1 = ChristmasPresent("Toy car", 10.5)
        present2 = ChristmasPresent("Doll", 15.2)
        self.person.AddPresent(present1)
        self.person.AddPresent(present2)
        self.assertAlmostEqual(self.person.GetTotal(), 25.7, places=2)

if __name__ == '__main__':
    unittest.main()