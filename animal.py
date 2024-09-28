class Animal:
    def __init__(self, name:str, sound:str):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f'The {self.name} makes a {self.sound} sound.')


dog = Animal("dog","bark")
dog.make_sound()