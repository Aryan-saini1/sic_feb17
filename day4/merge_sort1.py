def merge_sort(numbers, low, high):
    if low < high:
        mid = (low + high) // 2  
        merge_sort(numbers, low, mid)
        merge_sort(numbers, mid + 1, high)
        merge(numbers, low, mid, high)
def merge(numbers, low, mid, high):
    array1 = numbers[low:mid + 1]  
    array2 = numbers[mid + 1:high + 1] 
    i = j = 0  
    k = low 
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            numbers[k] = array1[i]
            i += 1
        else:
            numbers[k] = array2[j]
            j += 1
        k += 1
    numbers[k:high + 1] = array1[i:] + array2[j:]
numbers=[int(i) for i in input().split()]
merge_sort(numbers,0,len(numbers))
print(numbers)