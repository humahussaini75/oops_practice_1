class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages, sex):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages
        self.sex=sex


    def printprog(self, name, salary, role, languages, sex):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}. and The sex {self.sex}"


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
humaira=Programmer("sarah", 50, "child", "all", "f")

shubham = Programmer("Shubham", 555, "Programmer", ["python"],"f")
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"],"m")
print(karan.no_of_holiday)


print(shubham.name, shubham.salary, shubham.role, shubham.languages)
print(karan.name, karan.salary, karan.role, karan.languages)
print(rohan.name, rohan.salary, rohan.role)
print(humaira.name, humaira.salary, humaira.role, humaira.languages,humaira.sex)
print(shubham.name, shubham.salary, shubham.role, shubham.languages, shubham.sex)
print(karan.name, karan.salary, karan.role, karan.languages, karan.sex)

k=Programmer("xyz",50,"abc","hindi", "g")
print(k.name, k.salary, k.role,k.languages,k.sex)
print(k)
print(k.no_of_holiday)
print(k.no_of_leaves)
k=Employee.no_of_leaves=889

print(Employee.no_of_leaves)
#kishwer=Employee("shiba", 7, "child", "one", "f") this will not work since this is not employee variables sex and langauages
#print(kishwer.name, kishwer.salary, kishwer.role, kishwer.sex)

kishwer=Programmer("shiba", 7, "child", "one", "f")
print(kishwer.name, kishwer.salary, kishwer.role, kishwer.sex)
kishwer = Programmer("lala",0,"role","chinease", "f")
#print(kishwer.name.kishwer.salary, kishwer.sex)
print(kishwer.printdetails())
print(f"name is {kishwer.name},and salary is {kishwer.salary}, and role is {kishwer.role}, and languages is only{kishwer.languages},and sex is {kishwer.sex}")
