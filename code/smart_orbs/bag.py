class Bag:
    '''This is a durable reusable shopping bag made out of biodegradable materials'''

    def __init__(self, id):
        '''Initializes the bag'''
        self.id = id  # Each bag has a unique ID so it can be tracked by the system
        self.life = 1.0  # Refers to the condition of the bag (1.0 = new, 0.0 = completely destroyed)
        self.clean = True  # Bags are either clean or dirty

    def explode(self):
        '''Occasionally a bag might explode'''
        self.life = 0
