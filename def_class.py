class Robot:
    '''this is to...'''
    def __init__(self, name, age):
        self.name = name
        self.age = age



robot1 = Robot('musaed',23)

print(robot1.__doc__)
print(robot1.name)
print(robot1.age)

print(robot1.__dict__)