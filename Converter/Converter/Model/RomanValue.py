from Utils import Codes as c
from re import (match, fullmatch,VERBOSE, compile, sub as substitute)

class RomanValue(object):

    def __init__(self,romanNumerals:str,*args:str,**kwargs:str)->None:

      if not isinstance(romanNumerals, str):
        raise TypeError("The roman numeral is not a string")
    
      if len(romanNumerals) == 0 or romanNumerals=='':
        raise TypeError("The roman numeral is empty")

      romanNumerals = romanNumerals.upper()

      if not self.__isValidCode(romanNumerals):
        raise TypeError("The roman numeral is not a valid")
     
      if not self.__isValidPattern(romanNumerals):
         raise TypeError("The roman numeral is not a valid pattern")

      self.value=romanNumerals


    def __isValidCode(self, romanNumerals:str)->bool:
        result = all(elem in c.Codes.getRomanCodes() for elem in romanNumerals)
        return result

    def __isValidPattern(self,romanNumerals:str)->bool:
       
            partial_numeral:str= romanNumerals
            for full_string, shortening in c.Codes.getRomanCodesShorterning():
                partial_numeral = substitute(
                r'%s$' % shortening,
                full_string,
                partial_numeral,
            )
            
                ##Thousand
                ### hundreds - ⅭⅯ (900), ⅭⅮ (400), ⅮⅭⅭⅭ (800), ⅭⅭⅭ (300)
                ### tens - ⅩⅭ (90), ⅩⅬ (40), ⅬⅩⅩⅩ (80), ⅩⅩⅩ (30)
                ## # ones - Ⅸ (9), Ⅳ (4), ⅤⅠⅠⅠ (8), ⅠⅠⅠ (3)
            ##return romanNumerals==partial_numeral
            patterns = compile(
                        '''
                        Ⅿ*                                       
                        ⅭⅯ|ⅭⅮ|Ⅾ?Ⅽ{0,3} 
                        ⅩⅭ|ⅩⅬ|Ⅼ?Ⅹ{0,3}
                        Ⅸ|Ⅳ|Ⅴ?Ⅰ{0,3}  
                        ''',
                        VERBOSE)

            result:bool = False


            if match(patterns, partial_numeral) is None:
                result=False
            else:
                result = True
                
                
            return result
            

    @property
    def getValue(self)->str:
      return self.value


