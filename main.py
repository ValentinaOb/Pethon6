from class1 import Person
from class2 import Student

print("N:")
n = int(input())

a=[]
for i in range(n):
    print("\nName:")
    name=input()
    print("Lastname:")
    lastname=input()
    print("Father:")
    father=input()
    print("Date:")
    date=input()
    print("Faculty:")
    faculty=input()
    print("Group:")
    group=input()
    print("Scholarship:")
    scholarship=int(input())
    print("Grade:")
    grade=float(input())

    a.append(Student(name,lastname,father,date, faculty, group,scholarship,grade))

ages=0
for i in range(n):
    ages+=int(a[i].age())

schls=0
for i in range(n):
    schls+=int(a[i].schl())

print("\nAge: ")
print(ages/n)
print("\nScholarship: ")
print(schls)

'''
s=Student("Nina","Kolin","Torald","09.12.1991","Legal","169",14235,99.7)
s1=Student("Petya","Trefd","Geron","25.02.1999","Legal","169",2453,60.5)
s2=Student("Rona","Apol","Quat","04.03.2000","Legal","169",4563,68.4)


print("\nAge: ")
print((s.age()+s1.age()+s2.age())/3)

print("\nScholarship: ")
print((s.schl()+s1.schl()+s2.schl())/3)


'''