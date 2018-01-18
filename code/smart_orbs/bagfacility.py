from bag import Bag
from random import random


class BagFacility:
    '''HQ for bag management system, where new bags are produced,
    used bags are cleaned, and unusable bags are composted'''

    def __init__(self):
        self.bag_count = 0
        self.compost_pile = []
        self.clean_bags = []

    def make(self):
        '''Make a new bag and add it to the set of clean bags'''
        self.bag_count += 1
        new_bag = Bag(self.bag_count)
        self.clean_bags.append(new_bag)
        return new_bag

    def clean(self, bag):
        '''Take a dirty bag and make it clean (cleaning places some wear and tear on the bag)'''
        bag.clean = True
        bag.life = bag.life - random(0.005, 0.05)
        self.clean_bags.append(bag)

    def compost(self, bag):
        '''Take a bag and put it in the compost pile'''
        self.compost_pile.append(bag)

    def intake(self, incoming_bags):
        '''From a set of incoming dirty bags, sort each bag based on whether it is suitable for cleaning and reusing,
        or whether it needs to be removed from circulation and composted'''
        cleaned_count = 0
        dead_count = 0
        for i in incoming_bags:
            if incoming_bags[i].life < 0.05:
                self.compost(incoming_bags[i])
                dead_count += 1
            else:
                self.clean(incoming_bags[i])
                cleaned_count += 1
        return dead_count

