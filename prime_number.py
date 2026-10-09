import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # Check factors from 5 up to sqrt(n), skipping even numbers
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

number = int(sys.argv[1])
prime = is_prime(number)

if prime:
    print("prime")
else:
    print("Not Prime")

