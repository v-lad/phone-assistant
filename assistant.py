from random import randint
from pprint import pprint
import pytest


def generate_random_numbers(numbers_count: int, code: str='', digits_count: int=12):
    need_digits = digits_count - len(code)

    return [int(code + ''.join(map(str, [randint(0, 9) for i in range(need_digits)]))) 
                for i in range(numbers_count)]


def find_numbers(db):
    template = input('Enter the number (or first few digits):\n')
    
    if 'inf' in template:
        return 'Invalid data'

    try:
        template = int(template)
        if template < 0:
            return 'It can`t be negative'
    except ValueError:
        return 'Invalid data'

    return [num for num in db if str(num).startswith(str(template))]


def startswith(string, template):
    pass    


def main():
    test_db = generate_random_numbers(100, '380')
    print(find_numbers(test_db))

if __name__ == "__main__":
    main()