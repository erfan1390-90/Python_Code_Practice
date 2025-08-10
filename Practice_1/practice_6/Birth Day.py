class Date_Birth_Day:
    def __init__(self,year1,year2,month1,month2,day1,day2):
        self.y1=year1
        self.y2=year2
        self.m1=month1
        self.m2=month2
        self.d1=day1
        self.d2=day2
        self.text=""
    def get_month_name(self):
        text=""
        month_type = ["Farvardin" ,"Ordibehesht" ,"Khordad" ,"Tir","Mordad","Shahrivar",
             "Mehr","Aban", "Azar", "Dey","Bahman" ,"Esfand"]
        if self.m2<=12 and self.m2>=1:
            text+=(month_type[self.m2-1])
        else:
            text+=("Month is out of the allowed range")
        return text
    def is_leap_year(self):
        text=''
        if ((self.y2)+1)%4==0:
            text+=("Leap Year")
        else:
            text+=("Not a Leap Year")
        return text
    def sub(self): 
        text=""
        year=self.y1-self.y2
        month=self.m1-self.m2
        day=self.d1-self.d2
        if day <0:
            month-=1
            day+=31
        if month<0:
            year-=1
            month+=12
        if year<0:
            text+=("The year is less than the acceptable range")  
        else:  
            text+=(f"Year: {year} | Month: {month} | Day: {day}")
        return text
while True:
    print("""
1=> Birth Day
2=> Exit
""")
    c=input("Enter choice: ")  
    if c=="1" :
        year1=int(input("Enter year 1: "))
        year2=int(input("Enter year 2: "))
        month1=int(input("Enter month 1: "))
        month2=int(input("Enter month 2: "))
        day1=int(input("Enter day 1: "))
        day2=int(input("Enter day 2: "))
        result=Date_Birth_Day(year1,year2,month1,month2,day1,day2)
        if year1>=0 and year2>=0 and year1<=9999 and year2<=9999:
            if month1<=12 and month2<=12 and month1>=0 and month2>=0 :
                if day1<=31 and day2<=31 and day1>=0 and day2>=0:    
                    print(f"""
        ************
valid date
{result.sub()}
month: {result.get_month_name()}
{result.is_leap_year()}
        ************
        """)
                else:
                            print("Day exceeds the maximum allowed value")
            else:
                        print("Month is out of the allowed range")
        else:
                    print("Year is out of the allowed range")
    elif c=="2":
         print("Goodbye")
         break
    else:
        print("Invalid choice")