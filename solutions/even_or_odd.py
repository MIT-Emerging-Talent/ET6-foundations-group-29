"""Finction to check if a number is odd or even
@author: msrak
"""

def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"number is odd"


num = int(input("Enter a number"))
result = check_even_or_odd(num)
print(result)