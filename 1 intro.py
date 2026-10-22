#  Add 2 list to a list
# l1 = [1,2,3,4,5]
# l2 = [2,3,4,5,6]
# l3 = []
# for i in range(len(l1)):
#     l3.append(l1[i] + l2[i])
# print(l3)

# Multiplication table
# number = int(input("Enter a number: "))
# for i in range(1,11):
#     value = number * int(i)
#     print(f"{number} * {i} = {value}")

# 1. Generate all even numbers between 1 and 50
for i in range(1,51):
    if i % 2 == 0:
        print(i)

# 2. Generate all odd numbers between 1 and 30
for i in range(1,31):
    if i % 2 != 0:
        print(i)
# or
# odd = [i for i in range(1,31) if i % 2 != 0]
# print(odd)

# 3. Extract all numbers greater than 25 from a list numbers = [10, 45, 20, 60, 15, 30, 80]
l2 =[]
numbers = [10, 45, 20, 60, 15, 30, 80]
for num in numbers:
    if num > 25:
        l2.append(num)
print(l2)

# 4. Create a list of numbers divisible by both 3 and 5 from 1 to 100
l1 = []
for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        l1.append(num)
print(l1)

# 5. Extract all words containing more than five characters words = ["apple", "banana", "elephant", "cat", "computer"]
l3=[]
words = ["apple", "banana", "elephant", "cat", "computer"]
for word in words:
    if len(word) > 5:
        l3.append(word)
print(l3)

# 6.Replace negative numbers with zero , numbers = [10, -5, 20, -8, 0, 15, -2]
l4 =[]
numbers = [10, -5, 20, -8, 0, 15, -2]
for num in numbers:
    if num < 0:
        num = 0
        l4.append(num)
    elif num > 0:
        l4.append(num)
print(l4)








