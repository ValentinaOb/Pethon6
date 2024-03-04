from class1 import Person

class Student(Person):

    def __init__(self,name,lastname,father,date, faculty, group,scholarship,grade):
        self.name = name
        self.lastname = lastname
        self.father = father
        self.date = date
        self.faculty = faculty
        self.group = group
        self.scholarship = scholarship
        self.grade=grade
    
    def schl(self):
        return self.scholarship
