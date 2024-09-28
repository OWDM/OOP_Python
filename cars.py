class Car:
    def __init__(self, brand:str, model:str, year:int=2000):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        print(f'This car is a {self.year} {self.brand} {self.model}')
    

#CAR = Car("TOYOTA",'YARES')
#CAR.description()

car2 = Car("yy","enfe",2015)
car2.description()