def partition(numbers):
    j=0
    pivot_element=numbers[-1]
    for i in range(len(numbers)):
        if numbers[i]<pivot_element:
            numbers[i],numbers[j]=numbers[j],numbers[i]
            j+=1
    numbers[j],numbers[-1]=numbers[-1],numbers[j]
print("Enter the input numbers:")
numbers=list(map(int,input().split()))
partition(numbers)
print(f"Sorted array is:{numbers}")