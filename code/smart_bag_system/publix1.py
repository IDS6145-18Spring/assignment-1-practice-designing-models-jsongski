
from store import Store


class Publix1(Store):
    '''Publix located in Town Park'''
    def __init__(self, name, location, use_rate, bag_demand, return_rate):
        self.use_rate = 700
        self.return_rate = 0.85
        Store.__init__(self, name, location, use_rate, bag_demand, return_rate)

    publix1 = Store('Publix Town Park', 'E. Colonial', 10000, 8000)
