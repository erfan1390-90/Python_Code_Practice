print("welcome")
def min(a):
    ae=(a//60)
    return ae
def hou(a):
    ad=(a//3600)
    return ad

a3=int(input("Enter the second: "))
a1=hou(a3)
a2=min(a3-a1*3600)
a4=a3-(a1*3600)-(a2*60)
print(a1,":",a2,":",a4)