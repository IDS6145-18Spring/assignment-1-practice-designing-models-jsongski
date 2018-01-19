import random
import numpy as np
from bag import Bag
from bagfacility import BagFacility
from customer import Customer
from kiosk import Kiosk
from store import Store

# Set up Bag HQ
bag_hq = BagFacility()


def make_humans(count):
    '''Create some random shoppers'''
    customers = []
    for i in range(1, count + 1):
        shop_day = random.randint(0, 6)  # Assign customer a designated shopping day (0 = Sunday, 6 = Saturday)
        bag_use = random.randint(1, 10)  # Number of bags customer uses per trip
        motiv = random.randint(1, 10)  # Customer's level of motivation to participate in SmartORBS
        conscient = random.randint(1, 10)  # Customer's conscientiousness
        customers.append(Customer(i, shop_day, bag_use, motiv, conscient))
    return customers


def build_kiosks(count):
    '''Set up some bag return kiosks'''
    kiosks = []
    for i in range(1, count + 1):
        kiosks.append(Kiosk(i))
    return kiosks


def first_bags(count):
    '''Produce initial bag batch'''
    clean_bags = []
    for i in range(1, count + 1):
        clean_bags.append(Bag(i))
    return clean_bags


def replace(deadbags):
    '''Replace composted bags with new bags'''
    for i in range(1, deadbags):
        bag_hq.make()


def main():
    humancount = int(input('Select number of customers to simulate: '))
    kioskcount = int(input('Select number of kiosks to simulate: '))
    bagcount = int(input('Select starting bag amount: '))
    dist = int(input('Select how many bags to distribute per store: '))

    cust = make_humans(humancount)
    for human in cust:
        human.info()

    kiosks = build_kiosks(kioskcount)

    start_bags = first_bags(bagcount)
    for bag in start_bags:
        bag.info()

    # Set up existing Publices
    pub_tpark = Store('Publix Town Park', 'E. Colonial', 2)
    pub_cpark = Store('Publix College Park', 'Edgewater', 1)
    pub_eola = Store('Publix Lake Eola', 'E Central', 3)
    pub_dphil = Store('Publix Dr. Phillips', 'Dr. Phillips', 4)

    publices = [pub_tpark, pub_cpark, pub_eola, pub_dphil]
    for publix in publices:
        publix.info()
        publix.inventory()

    print(f'\nSmartORBS distributed {dist} bags to each store.\n')

    # Distribute initial bag supply
    for publix in publices:
        deliver = random.sample(start_bags, dist)
        publix.receive(deliver)
        print(publix.inventory())


#    deadbags = bag_hq.intake(returned_bags)
#    replace(deadbags)

if __name__ == '__main__':
    main()
