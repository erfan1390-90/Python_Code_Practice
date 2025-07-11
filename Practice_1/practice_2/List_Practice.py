print("welcome")
a=[]
for i in range(20):
    a1=(float(input("Enter a number: ")))
    a.append(a1)
    a[i]=a[i]**2
a.sort()
print(a)
print(a[0],"and",a[19])
