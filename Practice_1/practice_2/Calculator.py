print("welcome")
def sum(a2,a3):
    ab=a2+a3
    return ab
def mul(a2,a3):
    ae=a2*a3
    return ae
def div(a2,a3):
    ag=a2/a3
    return ag
def sub(a2,a3):
    ap=a2-a3
    return ap
def pow(a2,a3):
    ad=a2**a3
    return ad
while True:
    print("""Select option
    + : Sum of two numbers
    - : Subtracting two numbers
    * : Multiplication of two numbers
    / : Dividing two numbers
    ** : Exponentiation of two numbers """)
    a1=(input("Which option do you choose? "))
    a2=(float(input("Enter the first number: ")))
    a3=(float(input("Enter the second number: ")))
    if a1=="+":
        print(sum(a2,a3))
    elif a1=="**":
        print(pow(a2,a3))       
    elif a1=="*":
        print(mul(a2,a3))
    elif a1=="/":
        print(div(a2,a3))
    elif a1=="-":
        print(sub(a2,a3))
    elif a1=="b":
        break
    else:
        print("No instructions found.")
    a4=input("Do you want the program to end? Yes or No: ")
    if a4=="No":
        print("The program is running again.")
    elif a4=="Yes":
        print("Goodbye")
        break
    else:
        break

