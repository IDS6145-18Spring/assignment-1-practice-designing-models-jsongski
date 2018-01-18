from random import randint
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
    for i in range(1, count):
        shop_day = randint(0, 6)  # Assign customer a designated shopping day (0 = Sunday, 6 = Saturday)
        bag_use = randint(1, 10)  # Number of bags customer uses per trip
        motiv = randint(1, 10)  # Customer's level of motivation to participate in SmartORBS
        conscient = randint(1, 10)  # Customer's conscientiousness
        customers.append(Customer(i, shop_day, bag_use, motiv, conscient))
    return customers


def build_kiosks(count):
    '''Set up some bag return kiosks'''
    kiosks = []
    for i in range(1, count):
        kiosks.append(Kiosk(i))
    return kiosks


def first_bags(count):
    '''Produce initial bag batch'''
    clean_bags = []
    for i in range(1, count):
        clean_bags.append(Bag(i))
    return clean_bags


def replace(deadbags):
    '''Replace composted bags with new bags'''
    for i in range(1, deadbags):
        bag_hq.make()


def main():
    cust = make_humans(10)
    for human in cust:
        human.info()

    kiosks = build_kiosks(1)

    start_bags = first_bags(100)

    #  Set up existing Publices
    pub_tpark = Store('Publix Town Park', 'E. Colonial', 2)
    pub_cpark = Store('Publix College Park', 'Edgewater', 1)
    pub_eola = Store('Publix Lake Eola', 'E Central', 3)
    pub_dphil = Store('Publix Dr. Phillips', 'Dr. Phillips', 4)


    deadbags = bag_hq.intake(returned_bags)
    replace(deadbags)

if __name__ == '__main__':
    main()
