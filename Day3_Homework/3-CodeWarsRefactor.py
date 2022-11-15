# Codewars - 'Find the odd int'
l1 = [1,2,2,3,3,3,4,3,3,3,2,2,1]
# Original Solution
def find_it(seq):
    num_dict = {}
    for number in seq:
        if number in num_dict.keys():
            num_dict[number] += 1
        else:
            num_dict[number] = 1
    for key, value in num_dict.items():
        if value % 2 != 0:
            return key
print(find_it(l1))

# Refactored Solutoin
# Refactored to improve time and space by removing 2 for loops and not requiring a dictionary for the result

def find_it2(seq):
    for number in seq:
        if seq.count(number) % 2 != 0:
            return number
print(find_it2(l1))
