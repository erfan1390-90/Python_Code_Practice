class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info_age(self):
        print(f"{self.name} is {self.age} years old")
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def walk(self):
        print(f"{self.name} is walking")
    def info_name(self):
        print(f"Her name is: {self.name}")
class Teacher(Human):
    def __init__(self,name,age,lesson):
        Human.__init__(self,name,age)
        self.lesson=lesson
    def lesson_m(self):
        print(f"{self.name} is teaching {self.lesson}")
class Student(Human):
    def __init__(self,name,age,average,home_work):
        Human.__init__(self,name,age)
        self.average=average
        self.home_work=home_work
    def GPA(self):
        print(f"{self.name}'s average grade is {self.average}")
    def home_work_m(self):
        print(f"{self.name}'s homework is in {self.home_work}")
output_t=Teacher(name="erfan",age=14,lesson="math")
print("<-->"*10)
print("Teacher information: ")
output_t.info_name()
output_t.info_age()
output_t.eat()
output_t.sleep()
output_t.walk()
output_t.lesson_m()
print("<-->"*10)
output_s=Student(name="ali",age=12,average=19,home_work="science")
print("Student information: ")
output_s.info_name()
output_s.info_age()
output_s.eat()
output_s.sleep()
output_s.walk()
output_s.home_work_m()
output_s.GPA()
print("<-->"*10)