#dog class exercises

class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        print(f'{self.name} says {sound}')

roxy = Dog('Roxy', 4)
ruby = Dog('Ruby', 1)

#tests

ruby.species = 'dorg'
print(ruby.species)

print(roxy)

print(ruby.speak('Worf worf'))

