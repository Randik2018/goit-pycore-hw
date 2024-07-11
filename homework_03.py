import re

def normalize_phone(phone_number):
    
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
    
    if not cleaned_number.startswith('+'):
        return '+38' + cleaned_number
    
    return cleaned_number

raw_numbers = [
    "067\t1/33 4567",
    "(095) 555-5678\n",
    "+380 44 123 4567",
    "38050///1234567",
    "    +38(050)124-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)