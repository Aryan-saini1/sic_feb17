from itertools import permutations
n=int(input("Enter a number:"))
n2=str(n)
res=None
for i in sorted(set(permutations(n2,len(n2)))):
    if i>tuple(n2):
        res=i
        break
if res==None:
    print("No number exist")
else:
    res="".join(res)
    print(int(res))