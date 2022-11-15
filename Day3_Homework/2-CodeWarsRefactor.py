# Codewars - 'Return Negative'

# Original Solution
def make_negative(number):
    if number >= 0:
        return -(number)
    else:
        return (number)
print(make_negative(7))


# Refactored Solution
# Refactored solution is constant vs linear in the original
def make_negative2(number):
    return -abs(number)
print(make_negative2(7))