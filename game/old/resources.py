class Token:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

class Resource:
    def __init__(self, name, cost, power_type, power_value):
        self.name = name
        self.cost = cost  # Dictionary with 'Energy' and/or 'Gold'
        self.power_type = power_type  # 'Physical', 'Mental', 'Social'
        self.power_value = power_value

class Move(Resource):
    def __init__(self, name, cost, power_type, power_value):
        super().__init__(name, cost, power_type, power_value)

class Ally(Resource):
    def __init__(self, name, cost, power_type, power_value):
        super().__init__(name, cost, power_type, power_value)
        
    def start_of_day_effect(self):
        print(f"{self.name} has no start of day effect")

class Object(Resource):
    def __init__(self, name, cost, power_type, power_value):
        super().__init__(name, cost, power_type, power_value)

    def start_of_day_effect(self):
        print(f"{self.name} has no start of day effect")