import math

# Codewars - 'You're a Square!'
n1 = 3
n2 = 25

# Original Solution
def is_square(n):    
    if n < 0:
        return False
    if n == 0:
        return True
    else:
        x = 1
        while x < n:
            m = x * x
            if m == n:
                return True
            elif m > n:
                return False
            else:
                x += 1
print(is_square(n1))
print(is_square(n2))


# Refactored Solution
# Refactored to remove nested statements and improve time complexity

def is_square2(n):
    return n >= 0 and (n**0.5) % 1 == 0

print(is_square2(n1))
print(is_square2(n2))