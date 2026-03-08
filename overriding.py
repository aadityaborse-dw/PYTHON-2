class Vehicle:
    def move(self):
        print("Vehicle is not moving")


class Car(Vehicle):
    def move(self):
        print("Driving onto the road")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")



c = Car()
c.move()

b = Bicycle()

b.move()
