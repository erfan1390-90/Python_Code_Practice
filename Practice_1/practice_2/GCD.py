print("welcome")
a=[]
for i in range(2):
    a1=(int(input("Enter a number: ")))
    a.append(a1)
a.sort()
for i in range(a[0],0,-1):
    if a[0]%i==0 and a[1]%i==0:
        break
print( "GCD: ",i)