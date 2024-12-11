class engine:
    """docstring for engine"""

    #class attribute
    engines_produced = 0

    def __init__(self, hp: int, rev: int):
        engine.engines_produced +=1
        self.hp = hp
        self.rev = rev
        self.running = False

    def start(self):
        self.running = True

    def print(self):
        print(f"hp: {self.hp}, rev: {self.rev}. Number of engines produces {engine.engines_produced}")

class equipment:

    def __init__(self, equipment_name):
        self.equipment_name = equipment_name


class vehicle_4wh:
    """docstring for vehicle_4wh"""

    #class attribute
    number_of_wheels = 4

    def __init__(self, seats: int, color: str):
        #self.engine1 = engine1
        self.seats = seats
        self.color = color
        self.parked = False

    def park(self):
        self.parked = True

    def un_park(self):
        self.parked = False

class car(vehicle_4wh):

    def __init__(self, engine1: engine, seats: int, color: str, reg_nr:int, equip: equipment):
        super().__init__(seats, color)
        self.engine1 = engine1
        self.reg_nr = reg_nr
        self.equip = list [equipment]
        self.equip.append(equip)

    def add_equipment(self, equip:equipment):
        self.equip.append(equip)
    
    def new_equipment(self, text):
        self.equip.append(equipment(text))

class garage:

    def __init__(self, name):
        self.name = name
        self.car_list = []

    def add_car(self, car_object):
        self.car_list.append(car_object)