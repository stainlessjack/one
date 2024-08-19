class Zone:
    def __init__(self, name, element_type):
        self.name = name
        self.element_type = element_type
        self.elements = []

    def add_element(self, element):
        if isinstance(element, self.element_type):
            self.elements.append(element)
        else:
            raise TypeError(f"Element must be of type {self.element_type}")

    @classmethod
    def setup_zone(cls, name, element_type):
        return cls(name, element_type)