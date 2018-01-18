class Store:
    def __init__(self, name, location, traffic):
        self.name = name
        self.location = location
        self.traffic = traffic
        self.bags = []

    def store_info(self):
        '''Statement about store'''
        info = f'{self.name} is located at {self.location}.'
        return info

    def receive(self, gimme):
        '''Receive shipment of clean bags and add it to existing clean bag inventory'''
        self.bags = self.bags + gimme

    def dispense(self):
        '''Dispense clean bags to customers'''
        vend = self.bags
        self.bags = []
        return vend
