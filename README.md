# Assignment 1 - Practice Designing Models

> * Participant name: Jihye Song
> * Project Title: Smart Orlando Reusable Bag System (SmartORBS)

## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![Image of Smart City](images/smartcity.png)

Single-use plastic (e.g., shopping bags, beverage containers, straws) pose a threat to the environment and public health. Plastic bags are particularly problematic because they are not accepted by Orlando's recycling program and must be taken to a designated location that accepts plastic bags for recycling, which makes recycling difficult..
Discarded plastic contributes to pollution and has threatened marine life.

![Image of dolphin with plastic bag. Source: http://www.businessinsider.com/hawaii-plastic-bag-ban-2015-7](images/dolphin_plastic)

(remove: States your motivation clearly: why is it important / interesting to solve this problem?)
(remove: Add real-world examples, if any)
(remove: Put the problem into a historical context, from what does it originate? Are there already some proposed solutions?)

Arguably, the most effective way to drastically reduce plastic bag consumption is through legislation, i.e., banning plastic bags. Such measures have nearly eliminated plastic bag use in cities like ____
However, plastic bag bans may not succeed, either because they do not pass due to lack of support, or if they are implemented, they may face opposition from consumers. For example, Chicago repealed its plastic bag ban 
Without legislation, stores can take on a key role in reducing demand for plastic bags by encouraging consumers to be more proactive in their sustainability efforts. Some stores offer financial incentives for bringing reusable bags (e.g., 5 cents per bag).

Sharing programs have been implemented to promote sustainability and health, such as car sharing and bike sharing programs. 

## Requirements (Experimental Design)

(remove: You should start by specifying a set of requirements. I specified a topic Smart Cities but what exactly does that mean-  you should practice formulating your own set of requirements and an experiment. 
Define a hypothesis of a problem cities face and how a smart city would possibly help alleviate this issue. This helps you think about your problem communication and system objectives inputs, functions, and outputs - they should be clearly specified.)
The Smart Orlando Reusable Bag System shall:
* Automatically manage supply of reusable bags in circulation
  * Track location of each bag, as well as its condition
  * Clean used bags to reduce threats to health due to bacteria
  * Detect amount of bags needed by each store and deliver required number of bags
  * Detect when bags are at the end of their life cycle and remove them from circulation by composting them
* Only produce the amount of new bags to meet demand

* The system will also include an automated delivery system to ensure bags are transported on time as needed 
  * Autonomous bag transporting vehicles will collect dirty bags to deliver to Bag HQ, and deliver clean bags to stores

Additionally, the system will include a mobile app to engage participating customers. The app (and user interface at kiosks and stores) shall:
* Provide customers with up-to-date information about their bag use (updated once a day)
  * Remind customers to return used bags
  * Provide visualization of environmental impact (e.g., number of plastic bags kept out of the environment, carbon footprint, etc.)
  * Offer incentives to participate, including:
    * Points
    * Leaderboards to compete with friends
    * Discounts and coupons from the store based on participation

The system shall increase reusable bag use in participating stores relative to similarly-sized stores without the program. The system shall maintain adequate supply of bags (i.e., stores will not run out and new bags will be created when necessary)to ensure bags are always available for customers.

Reusable shopping bags may not be used by consumers despite widespread availability. Barriers to regular use include having to purchase bags. However, relatively inexpensive bags are offered by stores, and even if consumers purchase reusable bags, they must remember to bring them to the store when they shop.
Additionally, reusable bags carry bacteria and consumers typically do not keep up with cleaning. Thus, despite a desire to reduce plastic bag use, reusable bags are less convenient than disposable alternatives and unless motivation to use them is high, consumers may continue to use plastic bags even if they are aware of the harmful effects of plastic waste on the environment. A smart reusable bag management system will provide a solution by making reusable bags more convenient to use, and by motivating consumers to participate using gamification. 

> Null hypothesis 1(H<sub>0</sub>1): The smart reusable bag management system will not increase consumers' use of reusable shopping bags.  
> Alternate Hypothesis 1(H<sub>A</sub>1): The smart reusable bag management system will increase consumers' use of reusable shopping bags.

> Null hypothesis 2(H<sub>0</sub>2): The smart reusable bag management system will not maintain sufficient supplies at each store (i.e., greater than or equal to the number of bags used by customers at a store).  
> Alternate Hypothesis 2 (H<sub>A</sub>2): The smart reusable bag management system will maintain sufficient supplies at each store (i.e., greater than or equal to the number of bags used by customers at a store).

The success of this system relies on efficient management of supplies, as well as an understanding of consumer behavior. The present model focuses on designing an automated inventory management system to provide a supply of clean bags to stores.

## Smart City SmartORBS Model


At a high level, the main parts of the model involve a delivery system using autonomous vehicles, an inventory management system that produces, cleans, distributes, and composts bags, and a motivational mobile app designed to encourage customers to participate in the reusable bag program.

To start, the current project focuses on the second part of the system, which manages production, distribution, cleaning, and composting of bags.

The links below depict the components of the system at different levels.

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of SmartORBS
* [**Class Diagram**](model/class_diagram.md) - provides details of SmartORBS inventory management
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of SmartORBS
* [**Agent / User case**](model/agent_usecase_diagram.md) - provides details of how a customer interacts with SmartORBS

## Smart City SmartORBS Simulation

The simulation will take initial values, such as a store's traffic, customer demand, and lifespan of an individual bag, and run over a period of time to represent the flow of bags through the system. Initially, customers are randomly assigned attributes like motivation and conscientiousness. Eventually, the simulation will take into account how realistic variations in human decision making and behavior alter their interaction with the system. For example, in an ideal world, the system would run smoothly only producing just as many bags as are composted. However, in real life, bags will likely be lost or stolen, so the simulation will have to account for loss and manage inventory accordingly.

For the inventory management portion of the system, discrete-event based simulation will be used. Inputs include initial values for customers, stores, kiosks, and an initial quantity of bags. Outputs include bag inventory and whether the system adequately supplies bags given factors like damage, loss, and theft. The simulation described here (see [**SmartORBS simulation**](model/README.md)) file in the analysis folder - which describe how you would simulate this - type of simulation, rough details -inputs, outputs - how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)


## Smart City (My Problem) Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/smart_orbs/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
