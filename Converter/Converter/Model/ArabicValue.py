from Utils import Codes


class ArabicValue(object):    
    
    def __init__(self, arabic:str, *args:str, **kwargs:str)-> None:
        print("ArabicValue init")

        try:
            arabic_value:int = int(arabic)
        except:
            raise TypeError("The arabic value could not be cast to an int")


        if not isinstance(arabic_value, int) or isinstance(arabic, bool):
            raise TypeError("The arabic number is not an interger")

        if not (0 < arabic_value < 4000):
            raise TypeError("The arabic number must be between 1 and 3999")

        self.value:int = int(arabic_value)

    @property
    def getValue(self)->int:
        return self.value
