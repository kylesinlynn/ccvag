def validate(pan: str) -> bool:
    """Luhn Algorithms
    
    Check if the credit card is validated or not.
    
    pan: the credit card number
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