from random import random


class Customer:
    '''This is a human shopper'''

    def __init__(self, id, shop_days, bag_use, motiv):
        '''Set human attributes'''
        self.id = id
        self.shop_day = shop_days
        self.bag_use = bag_use
        self.bags = []

    def shop(self, gimme):
        for bag in gimme:
            bag.clean = False
            bag.life = bag.life - random(0.005, 0.05)
        self.bags = self.bags + gimme

    def dropoff(self):
        dirties = self.bags
        self.bags = []
        return dirties

    def lose(self):
