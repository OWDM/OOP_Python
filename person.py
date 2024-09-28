class Person:
    def __init__(self, name:str , age:int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    

Aperson = Person("Musaed", 23)
Aperson.greet()

