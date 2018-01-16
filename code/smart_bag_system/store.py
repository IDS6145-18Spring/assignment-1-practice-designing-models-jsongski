class Store:
    def __init__(self, name, location, use_rate):
        self.name = name
        self.location = location
        self.use_rate = use_rate
        self.bags = []

    def store_info(self):
        info = f'{self.name} is located at {self.location}. It dispenses {self.use_rate} bags per day and receives' \
               f' {self.return_rate} dirty bags per day.'
        return info

    def dispense(self):
        '''Dispense clean bags'''
        vend = self.bags
        self.bags = []
        return vend

    def count_bags(self):

publix1 = Store('Publix Town Park', 'E. Colonial', 10000, 8000)
publix2 = Store('Publix College Park', 'Edgewater', 8000, 7000)
publix3 = Store('Publix Lake Eola', 'E Central', 7000, 6500)
publix4 = Store('Publix Dr. Phillips', 'Dr. Phillips', 12000, 10000)
