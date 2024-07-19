class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self, animal):
        animal.make_sound()

    def eat(self, animal):
        print(f'{animal.name} is eating.')


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print('Chirp, chirp')