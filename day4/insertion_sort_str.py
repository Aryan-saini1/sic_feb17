import sys
def insertion_sort(string):
    n=len(string)
    for i in range(1,n):
        j=i-1
        element=string[i]
        while j>=0 and element.lower()<string[j].lower():
            string[j+1]=string[j]
            j-=1
        string[j+1]=element
    return string
input_string=sys.argv[1:]
print("Input string is:",input_string)
output_string=insertion_sort(input_string)
print("Output string is:",output_string)