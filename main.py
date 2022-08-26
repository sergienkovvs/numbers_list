import random

list_of_number = [random.randint(0,10) for nums in range(0,150)]

def get(list_of_number):
    nums = []

    for numbers in list_of_number:
        list_of_number.count(numbers)
        if numbers not in nums:
            print(numbers, list_of_number.count(numbers))
            nums.append(numbers)

get(list_of_number)
print(list_of_number)