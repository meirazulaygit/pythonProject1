class Student:
    def __init__(self, _id: str, name: str, grade: int):
        self._id = _id
        self.name = name
        self.grade = grade

    def checkPass(self):
        if self.grade < 70:
            return False

    def updateGrade(self):
        percent = int(input("enter percent of up garde"))
        grade = (self.grade * percent) / 100
        return grade


student1 = Student("5436554", 'koko', 64)
if student1.checkPass():
    print(f'hi {student1.name} Congratulations! your Passed')
else:
    print(f'hi {student1.name} your Failed, go to study')

student1.updateGrade()

print(f"my name is {student1.name}, dis is my id {student1._id} and it's my grade {student1.grade}")
