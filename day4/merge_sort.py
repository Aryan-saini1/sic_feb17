<<<<<<< HEAD
# Sum of Odd placed Even Digits
import sys

def sum_of_odd_placed_even_digits(number):
    sum1 = 0
    sum2 = 0
    flip = True
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit % 2 == 0:
            if flip:
                sum1 += digit
            else:
                sum2 += digit
        flip = not flip
    if flip:
        return sum2
    return sum1

input_number = int(sys.argv[1])
sum_of_digits = sum_of_odd_placed_even_digits(input_number)

print(f'Sum of Odd placed Even digits of {input_number} is {sum_of_digits}')
=======
def merge(numbers, low, mid, high):
    array1 = numbers[low : mid+1]
    array2 = numbers[mid+1 : high+1]

    i = 0
    j = 0
    k = low
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            numbers[k] = array1[i]
            i += 1
        else:
            numbers[k] = array2[j]
            j += 1
        k += 1
    numbers[k:high+1] = array1[i:] + array2[j:]
    # numbers[k:high+1] = array2[j:]

def merge_sort(numbers, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(numbers, low, mid)
        merge_sort(numbers, mid+1, high)
        merge(numbers, low, mid, high)

print('Enter the input numbers: ')
numbers = [int(num) for num in input().split()]

merge_sort(numbers, 0, len(numbers)-1)
print('Sorted Numbers are \n', numbers)
>>>>>>> 88ea2cf0ba99955422708c47807c543e254d0e82
