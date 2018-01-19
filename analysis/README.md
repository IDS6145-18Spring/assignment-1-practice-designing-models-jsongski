## Smart Orlando Reusable Bag System (SmartORBS) Simulation

**Discrete-event based simulation** can be used for the bag distribution and production system. However, **agent based simulation** would be useful when examining consumer behavior to determine the use/return rate for reusable bags.

The life cycle of reusable bags from production to circulation to composting can be tracked in discrete stages, making discrete-event based modeling suitable for the inventory tracking portion of the system. Agent based modeling can be used to simulate consumer behavior and decision making depending on features integrated into the system (e.g., a mobile app with motivational features such as reminders and incentives), as well as individual differences in customers (e.g., motivation, conscientiousness, forgetfulness, etc.).

Rather than having individual stores order bags on an ongoing basis, which would be inefficient for BagBot, clean and dirty bags will be delivered and collected on a weekly schedule following an optimized route to minimize fuel consumption.

For the discrete-event based simulation of the inventory management system, given some prior information that stores could provide, such as foot traffic, reusable bag use/return rate per store, as well as the failure rate/lifespan of each bag (i.e., what percentage of bags are damaged and need to be removed from circulation), the simulation can predict the flow of bags through the system.

Agent based modeling can be used to simulate how people make decisions to participate in the smart bag program. While real-life experimentation is a helpful way to determine how people will interact with the system, the benefit of simulation is that large-scale human behavior over time can be predicted. One challenge in social science research, particularly when it comes to behavior change, is that a typical laboratory study is too short to determine the effects of an intervention over time. Research in gamification has found that the initial novelty of motivational technologies may wear off (Hanus & Fox, 2015)<sup>1</sup>. Simulation can show how motivation increases and decreases over time.


<sup>1</sup> Hanus, M. D., & Fox, J. (2015). Assessing the effects of gamification in the classroom: A longitudinal study on intrinsic motivation, social comparison, satisfaction, effort, and academic performance. Computers & Education, 80, 152-161. https://doi.org/10.1016/j.compedu.2014.08.019
