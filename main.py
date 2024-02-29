
class Person:
    '''
    name="Name"
    lastname="Lastname"
    father="Father"
    date="04.01.2000"
    '''

    def __init__(self, name, lastname,father,date):
        self.name = name
        self.lastname = lastname
        self.father = father
        self.date = date

    def age(self):
        d=[]
        d=self.date.split(".")
        ages=2024-int(d[2])
        return ages

class Student(Person):
    '''
    faculty="facult"
    group="group"
    scholarship="1534"
    grade="47.6"
    '''
    def __init__(self, faculty, group,scholarship,grade):
        self.faculty = faculty
        self.group = group
        self.scholarship = scholarship
        self.grade=grade
    
    def schl(self):
        return self.scholarship

p=Person("Nina","Kolin","Torald","09.12.1991")
s=Student("Legal","169",14235,99.7)
s1=Student("Legal","169",2453,60.5)
s2=Student("Legal","169",4563,68.4)


print(p.age())

print("Scholarship: ")
print((s.schl()+s1.schl()+s2.schl())/3)


