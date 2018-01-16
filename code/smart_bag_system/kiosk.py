class Kiosk:
    '''This is a convenient location where customers can drop off used bags after shopping'''

    def __init__(self,):
        self.bags = []

    def collect(self, gimme):
        '''Receive used bags from customers'''
        self.bags = self.bags + gimme

    def empty(self):
        '''Empty kiosk for delivery to bag facility'''
        dirties = self.bags
        self.bags = []
        return dirties
