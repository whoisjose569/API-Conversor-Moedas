from fastapi import APIRouter
from converter import sync_converter

router = APIRouter()

@router.get('/converter/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')
    
    result = []
    
    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency = currency,
            price = price
        )
        
        result.append(response)
    
    return result