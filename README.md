# Python_simulation_for_queues_in_networks
This repository explain python simulation for any queue with arrival-service rates as geometric distribution/general distribution. Python script was developed to carry out empirical occupancy rates and average queue length over 100 million Markov states. 


# Project description

  This project deals with a discrete M/M/1 queue with arrival and service rate as geometric distributions. This queue is known as Geo/Geo/1 queue. 
  Selecting this queue gives some advantages to user to compute several important deciding factors regarding the queuing model. Several factors like average queue length, average time spent in the system, average waiting time for each packets and similar. 
  This project deals with occupancy rate and queue length of such queuing systems. This project also compares stationary distribution of the queuing systems with computed results. This helps determining the significance of the stationary distribution for such queue under different configurations. 

Environment for the project: 
•	Queue: Geo/Geo/1 queue was simulated on python to understand queuing statistics. 
•	Service rate: For Geo/Geo/1 queue simulation, service rate was kept at 0.5 with different arrival rates. 
•	Arrival rate:  any arrival rate can be configured to supervise the results.  
•	Numbers of servers: In this project simulation, number of server is one. (Geo/Geo/1)
•	Iterations: Since this project deals with discrete time queuing schemes, each process was calculated for 100 million time-slots. (100 million Markov states) 
•	An important condition for any queuing model to be stable is to have more service rate than inter-arrival rate. Therefore for any system to be stable, ‘inter-arrival rate < service rate’ condition is necessary. 

# Queue_length.py 

This python scipt gives out plot of avergage queue length vs theoretical queue length. 

•	Average of the queue length: This is an important factor while designing any queuing model. Using arrival-service rate distribution, average of the queue length can be found. This helps in designing the buffer sizes for the queue as it gives the results of average queue length. 
•	Empirical average of the queue length: This is the term used to show the computed average of the queue length using the python code. 
•	Theoretical average of the queue length: After determining ‘rho’ from any arrival-service distribution, average queue length of any systems can be found using the expectation theorem since it is using Geometric distribution. 
 
 
 # Occupancy_rate.py 
 
  This python code deals with Occupancy rate of the queuing models. This execution shows the occupancy rates for future states using Geo/Geo/1 queue and its stationary distribution formulas.  

•	Occupancy Rate: Occupancy rate is ratio of state being occupied to the total number of states. This could be an important factor in understanding queuing schemes. For this project, occupancy rate is calculated for each case to get better idea of how queuing system works with different arrival-service rates. Empirical occupancy and theoretical occupancy rates were carried out in python 3.0. 
•	Empirical occupancy rate: This is the occupancy rate calculated using python script. 
•	Theoretical occupancy rate:  Although it is an infinite geometric series but what makes it different than other series is the constant input rates. Mathematically, it is feasible to find stationary distributions using steady-state difference equation.
 





For more details : https://www.win.tue.nl/~iadan/queueing.pdf



