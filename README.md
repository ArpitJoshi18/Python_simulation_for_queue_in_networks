# Python_simulation_for_queue_in_networks
This repository explain python simulation for any queue with arrival-service rates as geometric distribution/general distribution. Python script was developed to carry out empirical occupancy rates and average queue length over 100 million Markov states. 


# Part 1 

This part deals with a discrete M/M/1 queue with arrival and service rate as geometric distributions. This queue is known as Geo/Geo/1 queue. Selecting this queue gives some advantages to user to compute several important deciding factors regarding the queuing model. Several factors like average queue length, average time spent in the system, average waiting time for each packets and similar. First part of the problem deals with occupancy rate of such queuing system and later queue length will be taken under consideration. To see different cases of the same project, three arrival-service distribution were picked to see results under high and low arrival rates. This project also compares stationary distribution of the queuing systems with computed results. This helps determining the significance of the stationary distribution for such queue under different configurations. 
Environment for the project: 
•	Queue: Geo/Geo/1 queue was simulated on python to understand queuing statistics. 
•	Service rate: For Geo/Geo/1 queue simulation, service rate was kept at 0.5 with different arrival rates. 
•	Arrival rate:  any arrival rate can be configured to supervise the results.  
•	Numbers of servers: In this project simulation, number of server is one. (Geo/Geo/1)
•	Iterations: Since this project deals with discrete time queuing schemes, each process was calculated for 100 million time-slots. (100 million Markov states) 
•	An important condition for any queuing model to be stable is to have more service rate than inter-arrival rate. Therefore for any system to be stable, ‘inter-arrival rate < service rate’ condition is necessary. 





