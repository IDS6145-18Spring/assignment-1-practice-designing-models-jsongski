class Store:
    def __init__(self, name, location, traffic):
        self.name = name
        self.location = location
        self.traffic = traffic  # Customer volume
        self.bags = []  # Bag inventory

    def info(self):
        '''Statement about store'''
        print(f'{self.name} is located at {self.location}. It has a traffic rating of {self.traffic}.')

    def inventory(self):
        '''Current inventory of bags'''
        print(f'{self.name} inventory: {len(self.bags)}')

    def receive(self, gimme):
        '''Receive shipment of clean bags and add it to existing clean bag inventory'''
        self.bags = self.bags + gimme

    def dispense(self):
        '''Dispense clean bags to customers'''
        vend = self.bags
        self.bags = []
        return vend
