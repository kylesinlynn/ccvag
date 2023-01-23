import unittest

from luhn import validate

class TestLuhnAlgorithm(unittest.TestCase):
    
    def test_credit_card(self):
        self.assertEqual(validate('4895048712071025'), True)
        
unittest.main()