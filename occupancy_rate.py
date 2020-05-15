import numpy as np
import matplotlib.pyplot as plt

average_arrival_rate = 0.4              #Arrival rate = 0.4
average_service_rate = 0.5              #Service rate/Departure rate = 0.5 
run_time = 10000000                     #Number of time-slots / number of Markov states 
q =np.zeros(run_time, dtype = int)
for i in range(len(q)):
    a = np.random.binomial(1, average_arrival_rate)
    s = np.random.binomial(1, average_service_rate)
    if i < len(q)-1:
        q[i + 1] = max(q[i] + a - s, 0)         #Queue(next-state) = Q(present-state) + Arrival(present-state) - Service(present-state)

max_queue_size = np.amax(q)
print(max_queue_size)

empirical_occupancy = np.zeros(max_queue_size+1)
for i in range(len(q)):
    empirical_occupancy[q[i]] = empirical_occupancy[q[i]]+1
empirical_occupancy = empirical_occupancy / run_time

rho = (average_arrival_rate * (1 - average_service_rate)) / (average_service_rate * (1 - average_arrival_rate))
theoretical_occupancy = np.zeros(max_queue_size + 1)                
for i in range(len(theoretical_occupancy)):
    theoretical_occupancy[i] = (rho**i)*(1-rho)         #Equation of theoretical equation to find occupancy rate / stationary equation

t = np.arange(0, max_queue_size+1, dtype=int)
plt.scatter(t, empirical_occupancy)
plt.scatter(t, theoretical_occupancy)
plt.show()
