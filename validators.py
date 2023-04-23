from datetime import date
from constants import POSSIBLE_CURRENCY_CODES

#Validators
def check_date(date_:str)->bool:
    """Function checking if the given date is in correct format"""
    try:
        date.fromisoformat(date_)
        return True
    except:
        return False
    
def check_num_of_last_quot(num_of_last_quot:int)->bool:
    """Function checking if the given number of last quotations is in correct range"""
    return False if num_of_last_quot>255 else True

def check_currency_code(currency_code:str)->bool:
    """Function checking if the given currency code is avaible"""
    return False if currency_code not in POSSIBLE_CURRENCY_CODES else True