# CORRECT SPECIFICATION:
#
# isPrime checks if a positive integer is prime.
#
# A positive integer is prime if it is greater than 
# 1, and its only divisors are 1 and itself.
#
# TASKS:
#
# 1) Add an assertion to test() that shows
#    isPrime(number) to be incorrect for 
#    some input.
#
# 2) Write isPrime2(number) to correctly 
#    check if a positive integer is prime.
# 
# Modified by Thiago Figueiró at 23/11/2015
# - change range(3,int(math.sqrt(number))) to range(3,int(math.sqrt(number)) + 1)
# The code is now correct!

import math

def isPrime(number):
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number))):  
        if (number%check) == 0:  
            return False
    return True

def isPrime2(number):  
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number)) + 1):  
        if (number%check) == 0:  
            return False
    return True

    pass

def test():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    
    # Before the modification, this nonPrime was returning a True
    assert isPrime(529) == False

    pass
