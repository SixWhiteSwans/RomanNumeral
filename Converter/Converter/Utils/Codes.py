from typing import (Tuple, Set, Dict,List)
from re import (VERBOSE, compile)

class Codes(object):
    """description of class"""

    @staticmethod
    def getRomanCodes()->List[str]:
         return ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I'] 
    
    @staticmethod
    def getCodes()->str:
        return 'MDCLXIIXIXIXVIIIXIIXIXIIIIII'
    #ⅯⅮⅭⅬⅫⅪⅩⅨⅧⅦⅥⅤⅣⅢⅡⅠ
    
    #lower case
    #ⅿⅾⅽⅼⅻⅺⅹⅸⅷⅶⅵⅴⅳⅲⅱⅰ

    @staticmethod
    def getRomanCodesShorterning()->List[Tuple[str,str]]:
         return [('XII','XII'),('XI','XI'),('VII','VII'),('VII','VII'),('VI','VI'),('III','III'),('II','II')] 

    @staticmethod
    def getMappingCodes()->List[Tuple[int,str]]:
         return [(1000,'M'), (900,'CM'),  (500,'D'), (400,'CD'), (100,'C'),  (90,'XC'), (50,'L'),  (40,'XL'), (10,'X'),  (9,'IX'),   (5,'V'),  (4,'IV'),   (1,'I')]

    @staticmethod
    def getPattern()->str:
        return ""

        #return compile(
        #    """
        #    M*                # thousands
        #    (CM|CD|D?C{0,3})  # hundreds - ⅭⅯ (900), ⅭⅮ (400), ⅮⅭⅭⅭ (800), ⅭⅭⅭ (300)
        #    (XC|XL|L?X{0,3})  # tens - ⅩⅭ (90), ⅩⅬ (40), ⅬⅩⅩⅩ (80), ⅩⅩⅩ (30)
        #    (IX|IV?Ⅰ{0,3})   # ones - Ⅸ (9), Ⅳ (4), ⅤⅠⅠⅠ (8), ⅠⅠⅠ (3)
        #    """,
        #    VERBOSE
        #)

    @staticmethod
    def getArabicCode()->Dict[str,int]:
      return {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
      
   

