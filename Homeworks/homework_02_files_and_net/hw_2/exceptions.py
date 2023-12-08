"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


def get_LoadOilTank(loadoiltank):
    if 0 < loadoiltank <= 30:
        raise LowFuelError(loadoiltank)
    elif 30 < loadoiltank <= 100:
        raise NotEnoughFuel(loadoiltank)
    elif loadoiltank >= 100:
        raise CargoOverload(loadoiltank)
    pass


def validate_LoadOilTank(Oil_Tank):
    pass


class ValidationError(Exception):
    pass


class LowFuelError(ValidationError):
    pass


class NotEnoughFuel(ValidationError):
    pass


class CargoOverload(ValidationError):
    pass


def load_oil_tank(Oil_Tank):
    try:
        loadoiltank = get_LoadOilTank(Oil_Tank)
        validate_LoadOilTank(Oil_Tank)
    except LowFuelError as e:
        print('!!! Low Fuel Level',e)
        exit(2)
    except NotEnoughFuel as e:
        print('!!! Not Enough Fuel',e)
        exit(2)
    except CargoOverload as e:
        print('!!! Cargo Over Load',e)
        exit(2)
    except Exception as e:
        print('!!! smth wrong',e)
        exit(1)
    else:
        exit(0)


# load_oil_tank(101)

