# Author: Sara Ghandehari

def factorial(n):
    """
    factorial(n) calculates factorial of integer number as n*(n-1)*(n-2)*...*1
    with recursive function.
    :param n: integer input
    :return: factorial value of type int
    """
    if n <= 1:
        return 1
    fact = n * factorial(n - 1)
    return fact

# Author: Nikoo Sabzevar
def factorial0(n):
    a = 1
    for i in range(1, n + 1):
        a = a * i
    return a


number = 10
print("The factorial of " + str(number) + " is equal to " + str(factorial(10)))
