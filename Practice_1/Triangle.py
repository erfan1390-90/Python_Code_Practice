print("welcome")
a1=int(input("Enter side one: "))
a2=int(input("Enter side two: "))
a3=int(input("Enter side three: "))
if(a1<(a2+a3)and a2<(a1+a3) and a3<(a1+a2)):
    print("This is triangle")
else:
    print("A triangle is not formed")