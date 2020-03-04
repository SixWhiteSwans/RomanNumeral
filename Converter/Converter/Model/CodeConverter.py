from Model.ArabicValue import ArabicValue as arabic
from Model.RomanValue import RomanValue as roman
from Model.ConvertFromArabicToRomanNumeral import ConvertFromArabicToRomanNumeral as converter_roman
from Model.ConvertFromRomanNumeralToArabic import ConvertFromRomanNumeralToArabic as converter_arabic

from functools import partial
from itertools import cycle

class CodeConverter(object):
   def Convert_ToRoman(self, value:str)->str:
        data:arabic = arabic(value)
        return converter_roman.convert(data)
       
   def Convert_ToArabic(self, value:str)->str:
        data:roman = roman(value)
        return str(converter_arabic.convert(data))
   
