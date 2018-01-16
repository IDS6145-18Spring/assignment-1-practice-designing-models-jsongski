class Bag:
    '''This is a reusable shopping bag made out of biodegradable materials'''

    def __init__(self, id):
        '''Intializes the bag'''
        self.id = id
        self.life = 1.0
        self.clean = True

    def explode(self):
        '''Occasionally a bag might explode'''
        self.life = 0
