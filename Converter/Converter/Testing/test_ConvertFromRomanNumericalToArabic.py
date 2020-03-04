import unittest
from Model.RomanValue import RomanValue as dataValidation
from Model.ConvertFromRomanNumeralToArabic import ConvertFromRomanNumeralToArabic as converter

class Test_ConvertFromRomanNumericalToArabic(unittest.TestCase):
     def test_Conversion(self)->None:
        data:dataValidation = dataValidation('M')
        result:int = converter.convert(data)
        self.assertEquals(1000, result,"CorrectValue")

if __name__ == '__main__':
    unittest.main()
