## convert numbers into list
numbers = list(range(1,10))
print(numbers)

odd_numbers = list((range(1,101,2)))
print(odd_numbers)

squares = []
for value in range(1,11):
    sqaure = value ** 2
    squares.append(sqaure)
print(squares)

digits = [1,2,3,4,5,6]
# print(min(digits))
# print((max(digits))
print(sum(digits))