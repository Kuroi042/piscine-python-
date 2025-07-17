import math

def NULL_not_found(object: any) -> int:
    """
    Function that prints the object type of all types of "Null".
    Returns 0 if it goes well and 1 in case of error.
    """
    try:
        # Check for None
        if object is None:
            print("Nothing: None <class 'NoneType'>")
            return 0
        
        # Check for NaN (Not a Number)
        elif isinstance(object, float) and math.isnan(object):
            print("Cheese: nan <class 'float'>")
            return 0
        
        # Check for Zero
        elif object == 0 and isinstance(object, int):
            print("Zero: 0 <class 'int'>")
            return 0
        
        # Check for Empty string
        elif object == '' and isinstance(object, str):
            print("Empty:  <class 'str'>")
            return 0
        
        # Check for False boolean
        elif object is False and isinstance(object, bool):
            print("Fake: False <class 'bool'>")
            return 0
        
        # If none of the above, it's not a recognized NULL type
        else:
            print("Type not Found")
            return 1
            
    except Exception:
        print("Type not Found")
        return 1
    
# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))
