class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def say_hi(self):
        print("hi ", self.name)

    def say_major(self):
        print("your major is ", self.major)

if __name__ == "__main__":
    student = Student("Bryce", "Computer Science")
    student.say_hi()
    student.say_major()
