import unittest
from salary import calculateDiscountedPrice
class SalaryTests(unittest.testCase):
    def test_When_not_nember_and_cost_is_less_1000_then_price_is_unchange(self):
        #arrange
        isMember=False
        price=800
        #act
        result=calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEpual(result,800)
    def test_When_not_nember_and_cost_is_less_1000_price_unchange(self):
        #arrange
        isMember=True
        price=100
        #act
        result=calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEpual(result,98)
        def test_When_not_nember_and_cost_is_more_than_1000_price_unchange(self):
        #arrange
         isMember=False
        price=2000
        #act
        result=calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEpual(result,1900)

    def test_When_member_and_cost_is_more_than_1000_price_unchange(self):
    #arrange
       isMember=False
    price=2000
        #act
    result=calculateDiscountedPrice(price,isMember)
        #assert
    self.assertEpual(result,1890)

unittest.main()      