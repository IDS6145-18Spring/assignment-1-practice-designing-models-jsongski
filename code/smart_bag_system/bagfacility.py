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
        self.bag_count += 1
        new_bag = Bag(self.bag_count)
        self.clean_bags.append(new_bag)
        return new_bag

    def clean(self, bag):
        bag.clean = True
        bag.life = bag.life - random(0.005, 0.05)
        self.clean_bags.append(bag)

    def compost(self, bag):
        self.compost_pile.append(bag)

    def intake(self, incoming_bags):
        cleaned_count = 0
        dead_count = 0
        for i in incoming_bags:
            if incoming_bags[i].life < 0.05:
                self.compost(incoming_bags[i])
                dead_count += 1
            else:
                self.clean(incoming_bags[i])
                cleaned_count += 1
        for i in range(1, dead_count):
            self.make()
        return dead_count

deadbags = bag_hq.intake(incoming)
for i in range (1, deadbags):
    bag_hq.make()