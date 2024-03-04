class Person:

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
