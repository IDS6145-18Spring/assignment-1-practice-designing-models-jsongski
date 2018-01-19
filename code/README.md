## Smart Orlando Reusable Bag System (*SmartORBS*) Model

While the problem at hand is complex and multifaceted, the current project focuses on one part of it, an automated system that manages reusable bag supplies across participating stores. The system comprises a central bag management facility (Bag HQ), bags, stores, return kiosks, and customers.

The automated system will detect how many bags are needed to meet customer demand, and will track inventory over time to determine how many new bags need to be produced to meet demand.

Additionally, the system will track the location of each bag throughout its life cycle, clean bags before redistributing them, and detect when bags need to be removed from circulation due to wear and tear.

The simulation will be run in [**BagBot**](../code/smart_orbs/bagbot.py).

BagBot will take some initial information (e.g., a given number of customers, bags, stores, and kiosks) and simulate the exchange of bags as they interact with these components. First, the simulation can be adjusted to look at the outcome of varying customer populations, initial bag supplies, and buildings.

Given some other information that may need to be acquired through other experiments (e.g., using agent based simulation), such as customer decision making, the simulation can account for human behavior like loss or theft, as well as motivation due to mobile app use.
