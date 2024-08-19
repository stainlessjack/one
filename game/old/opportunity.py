class Opportunity:
    def __init__(self, type, subtype, name, description, availability, location, clock, obstacles=None, consequences=None, power_threshold=None, cost=None):
        self.type = type
        self.subtype = subtype
        self.name = name
        self.description = description
        self.availability = availability
        self.location = location
        self.clock = clock
        self.obstacles = obstacles or []
        self.consequences = consequences or {}
        self.power_threshold = power_threshold
        self.cost = cost
        self.claimed = False

    def tick(self):
        # Advance the clock and resolve if necessary
        pass

    def resolve(self):
        # Resolve the opportunity based on player engagement
        pass