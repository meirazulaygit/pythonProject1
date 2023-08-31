class Dog:

    def __init__(self, typee: str, color: str, age: int, trained: bool, name: str):
        self.typee = typee
        self.color = color
        self.age = age
        self.trained = False
        self.name = name

    def train(self):
        if self.trained == False:
            self.trained = True

    def bark(self):
        print(f'My name is {self.name} and i am {self.typee} dog, i have Beautiful {self.color} color and i am {self.age} is old ')


dog1 = Dog("podel", "black", 3, False, "rexi")
dog1.train()

print(dog1.name)
print(dog1.bark())


