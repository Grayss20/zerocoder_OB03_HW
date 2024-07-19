class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} is eating.')


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print('Chirp, chirp')


class Mammal(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

    def make_sound(self):
        print('Grrrrr')


class Reptile(Animal):
    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length

    def make_sound(self):
        print('Shhhhh')


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ZooKeeper(Employee):

    def __init__(self, name, age):
        super().__init__(name, age)

    def feed_animal(self, animal):
        animal.eat(self)


class Veterinarian(Employee):

    def __init__(self, name, age):
        super().__init__(name, age)

    def heal_animal(self, animal):
        print(f'{animal.name} is healing. {self.name} heals {animal.name}.')


class Zoo:
    def __init__(self, animals, employees):
        self.animals = animals
        self.employees = employees

    def add_bird(self):
        name, age, wingspan = input(print('Enter name, age and wingspan of new bird. Separate values with spaces')).split()
        self.animals.append(Bird(name, age, wingspan))

    def add_mammal(self):
        name, age, weight = input(print('Enter name, age and weight of new mammal. Separate values with spaces')).split()
        self.animals.append(Mammal(name, age, weight))

    def add_reptile(self):
        name, age, length = input(print('Enter name, age and length of new reptile. Separate values with spaces')).split()
        self.animals.append(Reptile(name, age, length))

    def add_zookeeper(self):
        name, age = input(print('Enter name and age of new zookeeper. Separate values with spaces')).split()
        self.employees.append(ZooKeeper(name, age))

    def add_veterinarian(self):
        name, age = input(print('Enter name and age of new veterinarian. Separate values with spaces')).split()
        self.employees.append(Veterinarian(name, age))


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Example usage

zoo = Zoo([], [])

zoo.add_bird()
zoo.add_mammal()
zoo.add_reptile()
zoo.add_zookeeper()
zoo.add_veterinarian()

zoo.animals[0].make_sound()
zoo.animals[1].eat()

zoo.employees[0].feed_animal(zoo.animals[0])
zoo.employees[1].heal_animal(zoo.animals[1])

animal_sound(zoo.animals)
