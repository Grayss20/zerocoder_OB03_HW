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
        print(f'{self.name} feeds {animal.name}.')
        animal.eat()


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
        name, age, wingspan = input('Enter name, age and wingspan of new bird. Separate values with spaces: ').split()
        self.animals.append(Bird(name, age, wingspan))

    def add_mammal(self):
        name, age, weight = input('Enter name, age and weight of new mammal. Separate values with spaces: ').split()
        self.animals.append(Mammal(name, age, weight))

    def add_reptile(self):
        name, age, length = input('Enter name, age and length of new reptile. Separate values with spaces: ').split()
        self.animals.append(Reptile(name, age, length))

    def add_zookeeper(self):
        name, age = input('Enter name and age of new zookeeper. Separate values with spaces: ').split()
        self.employees.append(ZooKeeper(name, age))

    def add_veterinarian(self):
        name, age = input('Enter name and age of new veterinarian. Separate values with spaces: ').split()
        self.employees.append(Veterinarian(name, age))

    def save_to_file(self):
        with open('birds.txt', 'w') as file_b:
            file_b.truncate()
            with open('mammals.txt', 'w') as file_m:
                file_m.truncate()
                with open('reptiles.txt', 'w') as file_r:
                    file_r.truncate()
                    for animal in self.animals:
                        if isinstance(animal, Bird):
                            file_b.write(f'{animal.name} {animal.age} {animal.wingspan}\n')
                        elif isinstance(animal, Mammal):
                            file_m.write(f'{animal.name} {animal.age} {animal.weight}\n')
                        elif isinstance(animal, Reptile):
                            file_r.write(f'{animal.name} {animal.age} {animal.length}\n')
                        else:
                            print('Unknown animal type')

        with open('zookeepers.txt', 'w') as file_z:
            file_z.truncate()
            with open('veterinarians.txt', 'w') as file_v:
                file_v.truncate()
                for employee in self.employees:
                    if isinstance(employee, ZooKeeper):
                        file_z.write(f'{employee.name} {employee.age}\n')
                    elif isinstance(employee, Veterinarian):
                        file_v.write(f'{employee.name} {employee.age}\n')
                    else:
                        print('Unknown employee type')

        print('All data saved to files birds.txt, mammals.txt, reptiles.txt, zookeepers.txt, veterinarians.txt.')

    def load_from_file(self):
        with open('birds.txt', 'r') as file:
            for line in file:
                name, age, wingspan = line.strip().split()
                self.animals.append(Bird(name, age, wingspan))

        with open('mammals.txt', 'r') as file:
            for line in file:
                name, age, weight = line.strip().split()
                self.animals.append(Mammal(name, age, weight))

        with open('reptiles.txt', 'r') as file:
            for line in file:
                name, age, length = line.strip().split()
                self.animals.append(Reptile(name, age, length))

        with open('zookeepers.txt', 'r') as file:
            for line in file:
                name, age = line.strip().split()
                self.employees.append(ZooKeeper(name, age))

        with open('veterinarians.txt', 'r') as file:
            for line in file:
                name, age = line.strip().split()
                self.employees.append(Veterinarian(name, age))

        print('All data loaded from files birds.txt, mammals.txt, reptiles.txt, zookeepers.txt, veterinarians.txt.')


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

print('lets perform some tests')
zoo.animals[0].make_sound()
zoo.animals[1].eat()

zoo.employees[0].feed_animal(zoo.animals[0])
zoo.employees[1].heal_animal(zoo.animals[1])

animal_sound(zoo.animals)

zoo.save_to_file()
zoo_new = Zoo([], [])
zoo_new.load_from_file()

print('lets perform the same tests. Check the consistency')
zoo_new.animals[0].make_sound()
zoo_new.animals[1].eat()

zoo_new.employees[0].feed_animal(zoo_new.animals[0])
zoo_new.employees[1].heal_animal(zoo_new.animals[1])

animal_sound(zoo_new.animals)
