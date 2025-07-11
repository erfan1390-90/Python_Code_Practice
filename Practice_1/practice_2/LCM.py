print("welcome")
a=[]
for i in range(2):
    a1=(int(input("Enter a number: ")))
    a.append(a1)
a.sort()
a4=a[1]
a6=a[0]*a[1]
for i in range(a4,a6,+1):
    if i%a[0]==0 and i%a[1]==0:
        break
print( "LCM: ",i)