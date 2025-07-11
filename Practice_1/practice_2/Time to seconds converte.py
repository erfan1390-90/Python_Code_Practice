print("welcome")
def min(a):
    ae=(a*60)
    return ae
def hou(a):
    ad=(a*3600)
    return ad
def sec(a):
    af=(a*1)
    return af
a1=(int(input("Enter the hour: ")))
a2=(int(input("Enter the minute: ")))
a3=int(input("Enter the second"))
a10=(hou(a1)+ sec(a3)+ min(a2))
print(a10)