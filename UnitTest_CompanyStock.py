import unittest
import CompanyStock

class TestCompanyStock(unittest.TestCase):
    #class to unittest CompanyName class append_data method from CompanySotck.py 
    
    def test_append_data_positiveIntigers(self):
        #test case to check values for positive integers
        A = CompanyStock.CompanyName()
        actual = A.append_data('1990','Jan',203)
        expected = "data appended"
        self.assertEqual(actual, expected)
        
    def test_append_data_negativeIntegers(self):
        #test case to check value for negative integers
        
        B = CompanyStock.CompanyName()
        actual = B.append_data('1990','Feb',-203)
        expected = "data appended"
        self.assertEqual(actual, expected)
        
    def test_append_data_string(self):
        #test case to check value for string
        
        C = CompanyStock.CompanyName()
        actual = C.append_data('1990','Mar','share')
        expected = "data appended"
        self.assertEqual(actual, expected)
        
        
if __name__ == '__main__':
    unittest.main()