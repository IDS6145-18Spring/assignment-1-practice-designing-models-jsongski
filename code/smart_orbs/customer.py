from random import random


class Customer:
    '''This is a human shopper'''

    def __init__(self, id, shop_day, bag_use, motiv, conscient):
        '''Set customer attributes'''
        self.id = id  # New customers are assigned an ID
        self.shop_day = shop_day  # Customer's designated shopping day
        self.bag_use = bag_use  # Number of bags the customer uses each trip
        self.motiv = motiv  # Customer's motivation to participate in program
        self.conscient = conscient  # Conscientiousness of customer
        self.bags = []  # Stash of bags customer currently possesses
        self.stolen = []  # Bags the customer has removed from circulation due to theft

    def info(self):
        '''Introduce customer'''
        print(f'Customer {self.id} shops on Day {self.shop_day}, and uses {self.bag_use} bags each trip.')

    def shop(self, gimme):
        '''Take required number of clean bags for this shopping trip, and adds these to any bags the customer already
        has (using a bag makes it dirty)'''
        for bag in gimme:
            bag.clean = False
            bag.life = bag.life - random(0.005, 0.05)
        self.bags = self.bags + gimme

    def dropoff(self):
        '''Return bags to a kiosk'''
        dirties = self.bags
        self.bags = []
        return dirties

    def lose(self):
        '''Sometimes we lose things'''
        lost = self.bags.pop(random.randrange(len(self.bags)))
        self.stolen.append(lost)
        return lost

#    def steal(self, bags):
#        '''The human will keep a bag for their own use and never return it'''
#        for bag in bags:
#            if self.motiv < 5 and self.conscient < 3:
#                steal =
