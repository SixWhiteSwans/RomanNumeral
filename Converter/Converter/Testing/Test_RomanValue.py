import unittest
from Model.ArabicValue import ArabicValue as dataValidation


class Test_RomanValue(unittest.TestCase):
    #def test_isNotInt(self)-> None:
    #    testValue:str = "MLC" 
    #    with self.assertRaises(TypeError): c(testValue)
    
    def test_InvalidNumber(self)-> None:
        testValue:str = '-1'       
        with self.assertRaises(TypeError): dataValidation(testValue)
        #("The roman numerial must be between 1 and 3999")

    def test_ValidGetValue(self)-> None:
        testValue:str = '1000'
        dv:dataValidation = dataValidation(testValue)
        
        self.assertEquals(testValue, str(dv.getValue),"Roman Numeral valid")

if __name__ == '__main__':
    unittest.main()


