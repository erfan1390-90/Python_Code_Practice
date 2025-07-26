class Date():
    def __init__(self):
        pass       
    def show(self,year1,month1,day1):
        if 9999>=year1>=0 :
            if month1<=12 and  month1>=0 :
                if day1<=31 and day1>=0 :
                    print(f"Date => Year: {year1} | Month: {month1} | Day: {day1}")
                else:
                    print("Day exceeds the maximum allowed value")
            else:
                print("Month is out of the allowed range")
        else:
            print("Year is out of the allowed range")
    def add(self,year1,year2,month1,month2,day1,day2):
        if(year1>=0 and year2>=0):
            if month1<=12 and month2<=12 and month1>=0 and month2>=0:
                if day1<=31 and day2<=31 and day1>=0 and day2>=0:
                    print(f"Year: {year1+year2} | Month: {month1+month2} | Day: {day1+day2}")
                else:
                    print("Day exceeds the maximum allowed value")
            else:
                print("Month is out of the allowed range")
        else:
            print("Year is out of the allowed range")
    def get_month_name(self,month3):
    
        month_type = {
            1: "Farvardin", 2: "Ordibehesht", 3: "Khordad", 4: "Tir", 5: "Mordad", 6: "Shahrivar",
            7: "Mehr", 8: "Aban", 9: "Azar", 10: "Dey", 11: "Bahman", 12: "Esfand"
        }

        if month3<=12 and month3>=1:
            print(month_type[month3])
        else:
            print("Month is out of the allowed range")
    def is_leap_year(self,year3):

        if ((year3)+1)%4==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    def sub(self,year1,year2,month1,month2,day1,day2):
        if(year1>=year2 and year1>=0 and year2>=0):
            if(month1>=month2 and month1>=0 and month2>=0):
                if(day1>=day2 and day1>=0 and day2>=0):
                    print(f"Year: {year1-year2} | Month: {month1-month2} | Day: {day1-day2}")
                else:
                    print("Day exceeds the maximum allowed value")
            else:
                print("Month is out of the allowed range")
        else:
            print("Year is out of the allowed range")

    def is_valid_data(self,year1,month1,day1):
        if 9999>=year1>=0 :
            if month1<=12 and  month1>=0 :
                if day1<=31 and day1>=0 :
                    print("Valid date")
                else:
                    print("Day exceeds the maximum allowed value")
            else:
                print("Month is out of the allowed range")
        else:
            print("Year is out of the allowed range")

result=Date()
while True:
        
    print("""
1=> Show date
2=> Add two dates
3=> Show month name
4=> Check leap year
5=> Subtract two dates
6=> Validate date
7=> Exit
    """)
    d=input("Enter choice: ")
    if d=="1":
        year1=int(input("Enter year: "))
        month1=int(input("Enter month: "))
        day1=int(input("Enter day: "))
        result.show(year1,month1,day1)
    elif d=="2":
        year1=int(input("Enter year 1: "))
        year2=int(input("Enter year 2: "))
        month1=int(input("Enter month 1: "))
        month2=int(input("Enter month 2: "))
        day1=int(input("Enter day 1: "))
        day2=int(input("Enter day 2: "))
        result.add(year1,year2,month1,month2,day1,day2)
    elif d=="3":
        month3=int(input("Enter month number: "))
        result.get_month_name(month3)
    elif d=="4":
        year3=int(input("Enter year: "))
        result.is_leap_year(year3)
    elif d=="5":
        year1=int(input("Enter year 1: "))
        year2=int(input("Enter year 2: "))
        month1=int(input("Enter month 1: "))
        month2=int(input("Enter month 2: "))
        day1=int(input("Enter day 1: "))
        day2=int(input("Enter day 2: "))
        result.sub(year1,year2,month1,month2,day1,day2)
    elif d=="6":
        year1=int(input("Enter year: "))
        month1=int(input("Enter month: "))
        day1=int(input("Enter day: "))
        result.is_valid_data(year1,month1,day1)
    elif d=="7":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
