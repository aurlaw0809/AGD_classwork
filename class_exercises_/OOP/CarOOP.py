class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'the {self.color} car has {self.mileage} miles'

red = Car('red', 30000)
blue = Car('blue', 20000)

print(red)
print(blue)

for car in (red, blue):
    print(car)
