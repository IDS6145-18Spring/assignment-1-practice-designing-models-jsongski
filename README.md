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
* Only produce the amount of new bags to meet demand
* Automatically detect when bags are at the end of their life cycle and remove them from circulation by composting them

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

> Null hypothesis (H<sub>0</sub>): The smart reusable bag management system will not increase consumers' use of reusable shopping bags.  
> Alternate Hypothesis (H<sub>A</sub>): The smart reusable bag management system will increase consumers' use of reusable shopping bags.

The success of this system relies on efficient management of supplies, as well as an understanding of consumer behavior. The present model focuses on designing an automated bag management system to provide a supply of clean bags to stores.

## Smart City SmartORBS Model

(remove: add a high-level overview of your model, the part below should link to the model directory markdown files)
(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## Smart City SmartORBS Simulation

The simulation will 
(remove: for part 3 add two to three sentences here and link the [**SmartORBS simulation**](model/README.md) file in the analysis folder - which describe how you would simulate this - type of simulation, rough details -inputs, outputs - how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)


## Smart City (My Problem) Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/smart_orbs/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
