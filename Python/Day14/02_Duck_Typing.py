class Car:
    def start(self):
        print("Car Started...")

class Bike:
    def start(self):
        print("Bike Started...")


def begin(obj):
    obj.start()

begin(Car())
begin(Bike())