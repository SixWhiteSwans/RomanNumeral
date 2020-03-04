import unittest
from re import (match, fullmatch,VERBOSE, compile, sub as substitute)
from Model.RomanValue import RomanValue as dataValidation
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

class Test_ArabicValue(unittest.TestCase):   
    #def test_isNotString(self)-> None:
    #    testValue:int = 10000 
    #    with self.assertRaises(TypeError):  ab(testValue)

    def test_isEmpty(self)-> None:
        testValue:str = ""
        with self.assertRaises(TypeError):  dataValidation(testValue)
    
    def test_isInvalidCode(self)-> None:
        testValue:str = "XZE"     
        with self.assertRaises(TypeError):  dataValidation(testValue)

    def test_isValidCode(self)-> None:
        testValue:str = "MC"
        ob:dataValidation = dataValidation(testValue)
        self.assertEquals(testValue, ob.getValue,"MD")

    def test_isValidCode_IX(self)-> None:
        testValue:str = "IX"
        ob:dataValidation = dataValidation(testValue)
        self.assertEquals(testValue, ob.getValue,"IX")

    def test_isValidCode_CD(self)-> None:
        testValue:str = "CD"
        ob:dataValidation = dataValidation(testValue)
        self.assertEquals(testValue, ob.getValue,"CD")
    def test_match(self)->None:
         pattern_match:Optional[Match[str]] = match(r'^(CM)', 'CMXXXIV')
         #r"^(%s)+" % 
         count:int = len(pattern_match.group())
         self.assertEquals(2, count,"Pattern Match")


    def test_fullmatch(self)->None:

         result:bool 
         if match(compile(
                        '''
                        Ⅿ*                                       
                        ⅭⅯ|ⅭⅮ|Ⅾ?Ⅽ{0,3} 
                        ⅩⅭ|ⅩⅬ|Ⅼ?Ⅹ{0,3}
                        Ⅸ|Ⅳ|Ⅴ?Ⅰ{0,3}  
                        ''',
                        VERBOSE),'MC') is None:
             result=False
         else:
             result=True

         
         self.assertEquals(result, True,"MC match")


if __name__ == '__main__':
    unittest.main()
