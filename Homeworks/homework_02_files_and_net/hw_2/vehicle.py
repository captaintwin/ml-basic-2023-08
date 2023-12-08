import exceptions


class Vehicle:
    MIN_LEVEL: int = 0

    def __init__(self, weight=None, started=None, fuel=None, fuel_consumption=None, distance=None):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.distance = distance

    @property
    def start(self):
        print()
        print('<<<<< method start is beginning >>>>>')
        print()
        if not self.started:
            print('Started: ', self.started)
            if self.fuel == self.MIN_LEVEL:
                print('Error is: LowFuelError')
                print('Fuel level: ', self.fuel)
                raise exceptions.LowFuelError
            else:
                self.started = True
                print('Fuel level: ', self.fuel)
                print('Started: ', self.started)

    @property
    def move(self):
        print()
        print('<<<<< method move is beginning >>>>>')
        print()
        # 30 liters per 100km, 0.3l - 1km
        self.fuel_consumption = self.distance * 0.3
        print('Necessary fuel value: ', self.fuel_consumption)
        print('Actual fuel value: ', self.fuel)
        if self.fuel >= self.fuel_consumption:
            self.fuel -= 0.3
            print('Next fuel value after 1 km: ', self.fuel)
            print('Status: Fuel level is enough for the distance')
        else:
            print('Error is: NotEnoughFuel')
            raise exceptions.NotEnoughFuel


# car = Vehicle(1500,False,55,1, 150)
# print('Overview: ', car.start, car.move)

# print(car.started)

# plane = Vehicle()

#     @property
#     def weight(self):
#         return self._weight
#
#     def started(self):
#         return self._started
#
#     def fuel(self):
#         return self._fuel
#
#     def fuel_consumption(self):
#         return self._fuel_consumption
#
# cargo_1 = Vehicle.start(1, 1, 0)
