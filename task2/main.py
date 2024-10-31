'import modules to work with strings and functions'
import re
from typing import Callable

def generator_numbers(text: str):
    'Function to extract numbers from text'
    numbers = re.findall(r'(?<=\s)[0-9]+\.[0-9]+(?=\s)', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    'Function to get sum of numbers in given text'
    total_income = sum(func(text))
    return total_income

#TEST   
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
#EOF