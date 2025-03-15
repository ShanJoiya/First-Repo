class student:
        grade = 12 
        name = "Penguin"


        def introduction(self):
               print("Hello, I am student")


        def details(self):
              print("My name is", self.name)
              print("I study in grade", self.grade)


ob = student()

ob.introduction()
ob.details()