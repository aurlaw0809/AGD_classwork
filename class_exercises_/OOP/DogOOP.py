#dog class exercises

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speaks(self):
        return f'{self.name} says "woof"'

rufus = Dog('Rufus', 20)
fido = Dog('Fido', 10)

class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        print(f'{self.name} barks {sound}')

class Labrador(Dog):
    def speak(self, sound = 'Worff potato'):
        super().speak(sound)

roxy = Labrador('Roxy', 4)
ruby = Labrador('Ruby', 1)
mabel = Dog('Mabel', 3)
mango = Labrador('Mango', 1)
ben = Labrador('Ben', 15)

#tests

print(ruby.species)

print(ruby.speak())

