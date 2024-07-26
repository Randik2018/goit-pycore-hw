import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r'\d+\.?\d*'
    for item in re.findall(pattern, text):
        yield float(item)


def sum_profit(text: str, func: Callable):
    return sum(e for e in func(text))


if __name__ == '__main__':
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
