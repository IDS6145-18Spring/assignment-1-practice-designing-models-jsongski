class Kiosk:
    '''This is a convenient location (e.g., next to existing recycling receptacles, outside of store entrances,
    in apartment complexes/university residence halls, etc.) where customers can drop off used bags after shopping'''

    def __init__(self, id):
        self.id = id
        self.bags = []

    def collect(self, gimme):
        '''Receive used bags from customers'''
        self.bags = self.bags + gimme

    def empty(self):
        '''Empty kiosk for delivery to bag facility'''
        dirties = self.bags
        self.bags = []
        return dirties
