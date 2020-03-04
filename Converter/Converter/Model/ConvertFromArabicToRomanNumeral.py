from Utils import Codes as c
from Model.ArabicValue import ArabicValue as arabic
from typing import (Callable, Tuple, Dict,List)
from re import (sub as substitute)
class ConvertFromArabicToRomanNumeral(object):
    """description of class"""
    def __init__(self, *args:str,**kwargs:str) -> None:
        pass
    
    @staticmethod
    def convert(data:arabic)->str:
        #https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593

        #return_list:List[str] = []
        #remainder:int = data.getValue
        #for integer, numeral in c.Codes.getMappingCodes():
        #    repetitions, remainder = divmod(remainder, integer)
        #    return_list.append(numeral * repetitions)
        #    numeral_string:str = ''.join(return_list)

        numeral_string:str = ConvertFromArabicToRomanNumeral.__get_numeral(data.getValue)
        numeral_string = ConvertFromArabicToRomanNumeral.__get_numeral_short_codes(numeral_string)

        #for full_string, shortening in c.Codes.getRomanCodesShorterning():
        #    numeral_string = substitute(
        #        r'%s$' % full_string,
        #        shortening,
        #        numeral_string,
        #)
                         
        return numeral_string

    @staticmethod
    def __get_numeral(dataValue: int)->str:
       remainder:int = dataValue
       return_list:List[str] = []
       for integer, numeral in c.Codes.getMappingCodes():
            repetitions, remainder = divmod(remainder, integer)
            return_list.append(numeral * repetitions)
            numeral_string:str = ''.join(return_list)

       return numeral_string


    @staticmethod
    def __get_numeral_short_codes(numeral_string: str)->str:
        for full_string, shortening in c.Codes.getRomanCodesShorterning():
            numeral_string = substitute(
                r'%s$' % full_string,
                shortening,
                numeral_string,
        )
                         
        return numeral_string