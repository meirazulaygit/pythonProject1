class Person:
    def __init__(self, name, age, numOfKids):
        self.name = name
        self. age = age
        self.numOfKids = numOfKids

    def hasChildren(self):
        if self.numOfKids == 0:
            return False

    def ageGroup(self):
        if 0 <= self.age <= 18:
            return "Child"
        elif 19 <= self.age <= 60:
            return "Adult"
        elif 61 <= self.age <= 120:
            return "Senior"
        else:
            return "your age is not correct"


person1 = Person("kofiko", 8, 0)
print(f'My name is {person1.name} and i am {person1.age} is old also i have {person1.age} children')
print(person1.hasChildren())
print(person1.ageGroup())
