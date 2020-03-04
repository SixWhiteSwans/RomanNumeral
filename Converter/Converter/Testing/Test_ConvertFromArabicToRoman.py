import unittest
from Model.ArabicValue import ArabicValue as dataValidation_arabic
from Model.ConvertFromArabicToRomanNumeral import ConvertFromArabicToRomanNumeral as converter_arabic
from Model.RomanValue import RomanValue as dataValidation_roman
from Model.ConvertFromRomanNumeralToArabic import ConvertFromRomanNumeralToArabic as converter_roman

from Model.CodeConverter import CodeConverter as converter

class Test_ConvertFromArabicToRoman(unittest.TestCase):
   
    def test_Conversion_Roman(self)->None:
        data:dataValidation_roman = dataValidation_roman('M')
        result:int = converter_roman.convert(data)
        self.assertEquals(1000, result,"CorrectValue")

    def test_Conversion_Roman_MCMXXIV(self)->None:
        data:dataValidation_roman = dataValidation_roman('MCMXXXIV')
        result:int = converter_roman.convert(data)
        self.assertEquals(1934, result,"CorrectValue")

    def test_Conversion(self)->None:
        data:dataValidation = dataValidation_arabic('1000')
        result:str = converter_arabic.convert(data)
        self.assertEquals('M', result,"CorrectValue")

    def test_Conversion_Roman_Value_1934(self)->None:
        data:dataValidation_roman = dataValidation_arabic('1934')
        result:str = converter_arabic.convert(data)
        self.assertEquals('MCMXXXIV',result,"CorrectValue")       

if __name__ == '__main__':
    unittest.main()
