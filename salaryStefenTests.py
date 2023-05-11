# from salaryStefen import Emplyoo
# emplyoo1=Emplyoo ("Nesrin",30, 100, 40,4000)
# emplyoo2=Emplyoo("Osama",35, 100, 40,4000)
# emplyoo3=Emplyoo("Mira",50, 100, 40,4000)
# emplyoo4=Emplyoo("Mareyh",30, 100, 0,100)
# print(emplyoo1.name,emplyoo1.age,emplyoo1.hourly_wage,emplyoo1.hours_worked,emplyoo1.salary)
# print(emplyoo2.name,emplyoo2.age,emplyoo2.hourly_wage,emplyoo2.hours_worked,emplyoo2.salary)
# print(emplyoo3.name,emplyoo3.age,emplyoo3.hourly_wage,emplyoo3.hours_worked,emplyoo3.salary)
# print(emplyoo4.name,emplyoo4.age,emplyoo4.hourly_wage,emplyoo4.hours_worked,emplyoo4.salary)

# import unittest
# from salaryStefen import Emplyoo 

# class emplyoo (unittest.TestCase):
#    def setup(self):
#      self.calcalateSalary=0
import unittest
from salaryStefen import calculateSalary
class TestCalculateSalary(unittest.TestCase):
    def test_no_bonus(self):
        # #assert 
        self.assertEqual(calculateSalary ('Osama', 20, 100, 40), 4000)

    def test_5_percent_bonus(self):
       #assert   
        self.assertEqual(calculateSalary('Mira', 30, 80, 50), 4240)

    def test_6_percent_bonus(self):
         #assert 
        self.assertEqual(calculateSalary('Nesrin', 50, 70, 60), 4488)

    def test_220_bonus(self):
         #assert 
        self.assertEqual(calculateSalary('Stefan', 35, 90, 45), 4270)

if __name__ == '__main__':
    unittest.main()
    

