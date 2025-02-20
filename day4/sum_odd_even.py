n=input("Enter a number:")
sum=0
for i in range(0,len(n),2):
    if int(n[i])%2==0:
        sum+=int(n[i])
print(sum)