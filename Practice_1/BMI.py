a1=float(input("Enter your height (cm): "))
a2=float(input("Enter your weight (kg): "))
a3=a2/((a1**2))*10000
print(a3)
if a3<18.5:
    print("Under weight")
elif 18.5<=a3<25:
    print("Normal")
elif 25<=a3<30:
    print("Over weight")
elif 30<=a3<35:
    print("Obese")
else:
    print("Extremely obese")