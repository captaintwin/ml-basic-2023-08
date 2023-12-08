import vehicle
import engine


class Car(vehicle.Vehicle):

    def __init__(self, weight=None, started=None, fuel=None, fuel_consumption=None, distance=None):
        super().__init__(weight, started, fuel, fuel_consumption, distance)
        self.pistons = None
        self.volume = None

    def __int__(self, _engine=None, volume=None, pistons=None):
        self._engine = engine
        self.volume = volume
        self.pistons = pistons

    @property
    def set_engine(self):
        print()
        print('<<<<< Engine setted >>>>>')
        print()
        self.volume = engine.Engine.volume
        self.pistons = engine.Engine.pistons
        _engine = 'Value: ' + str(self.volume) + '\n' + 'Pistons: ' + str(self.pistons)
        return print(_engine)


car_eng = Car()
print(car_eng.set_engine)

