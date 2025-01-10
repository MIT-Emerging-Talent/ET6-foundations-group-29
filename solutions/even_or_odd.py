# Finction to check if a number is odd or even

def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"number is odd"

# for the user
6num = int(input("Enter a number"))
result = check_even_or_odd(num)
print(result)