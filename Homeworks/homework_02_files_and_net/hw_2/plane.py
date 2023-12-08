import vehicle
import exceptions


class Plane(vehicle.Vehicle):

    def __init__(self, weight=None, cargo=None, max_cargo=None):
        super().__init__(weight)
        self.cargo = cargo
        self.max_cargo = max_cargo

    @property
    def load_cargo(self):
        print()
        print('<<<<< Validation of loadig >>>>>')
        print()
        if (self.cargo + self.weight) > self.max_cargo:
            raise exceptions.CargoOverload
        else:
            current_cargo = self.cargo + self.weight
            return print('previous weight is: ' + str(self.weight),
                         '\n' + 'added cargo is: ' + str(self.cargo),
                         '\n' + 'current cargo is: ' + str(current_cargo))

    def remove_all_cargo(self):
        print()
        print('<<<<< remove_all_cargo of loadig >>>>>')
        print()
        current_cargo = self.cargo
        self.cargo = 0
        return print('Cargo weight before unload: ' + str(current_cargo),
                     '\n' + 'Cargo weight after unload: ' + str(self.cargo))


plane = Plane(10, 40, 50, )
print(plane.load_cargo)
print(plane.remove_all_cargo())
