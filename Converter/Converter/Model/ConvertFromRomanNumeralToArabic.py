from Utils import Codes as c
from Model.RomanValue import RomanValue as roman
import re
import io
from typing import (
    Dict,
    List,
    Tuple,
    Set,  
    NamedTuple,
    IO,
    Pattern,
    Match,
    Text,
    Optional,
    Sequence,
    Iterable,
    Mapping,
    MutableMapping,
    Any,
)


class ConvertFromRomanNumeralToArabic(object):
    """description of class"""
    
    @staticmethod
    def convert(data: roman)->int:

        partial_numeral:str= data.getValue
        return_value:int = 0

        for i in range(len(partial_numeral)):
            code:str=partial_numeral[i]
            value = c.Codes.getArabicCode()[code]
            # If the next place holds a larger number, this value is negative
            if i+1 < len(partial_numeral) and c.Codes.getArabicCode()[partial_numeral[i+1]] > value:
                return_value -= value
            else: return_value += value



        #for integer, numeral in c.Codes.getMappingCodes():            
        #    pattern_match = ConvertFromRomanNumeralToArabic.__get_pattern_match(numeral, partial_numeral)
        #    if pattern_match:
        #        chars_matched:int = len(pattern_match.group())
        #        numerals_matched:int = chars_matched // len(numeral)
        #        return_value += numerals_matched * integer
        #        partial_numeral = partial_numeral[chars_matched:]

        return return_value


    @staticmethod
    def __get_pattern_match(numeral: str, partial_numeral: str)->Optional[Match[str]]:
        pattern:str = r"^%s" % numeral 
        pattern_match:Optional[Match[str]] = re.match(pattern, partial_numeral)
        return pattern_match       