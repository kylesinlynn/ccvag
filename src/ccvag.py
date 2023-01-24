from random import choice, randint
from datetime import datetime

def validator(pan: str) -> bool:
    """Credit Card Validator using Luhn Algorithm

    Args:
        pan (str): The number of the credit card.

    Returns:
        bool: If the credit card is valid or not.
    """
    card_numbers: list = [int(num) for num in pan]
    sum: int = 0
    
    for index in range(len(card_numbers)):
        digit: int = card_numbers[index]
    
        if index % 2 == 0:
            digit *= 2
    
            if digit > 9:
                digit -= 9
        sum += digit
    
    return sum % 10 == 0

def generator(bin: str, total: int=10) -> list:
    """Credit Card Generator

    Args:
        bin (str): The first-sixth number of the credit card.
        total (int, optional): Total credit card count. Defaults to 10.

    Returns:
        list: The list of the credit cards.
    """
    cards: list = []
    months: list = range(1, 13)
    
    while len(cards) < total:
        generated_random_number: str = f'{bin}{randint(0, 1000)}'
        
        if validator(generated_random_number):
            card: dict = {
                'number': generated_random_number,
                'month': choice(months),
                'year': datetime.today().year + randint(1, 5)
            }
            cards.append(card)
            
    return cards