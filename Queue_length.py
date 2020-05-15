import matplotlib.pyplot as plt
import numpy as np
import statistics

average_arrival_rate = 0.2
average_service_rate = 0.5

rho = (average_arrival_rate * (1 - average_service_rate)) / (average_service_rate * (1 - average_arrival_rate))  # rho

run_time = 500  #run time
q = np.zeros(run_time, dtype=int)
empirical_average_q = np.zeros(run_time)
empirical_queuelen = []
for i in range(len(q)):
    a = np.random.binomial(1, average_arrival_rate)
    s = np.random.binomial(1, average_service_rate)
    if i < len(q)-1:
        q[i+1] = max(q[i] + a - s, 0)
        Sum = sum(q)
        average = Sum / len(q)
        empirical_queuelen.append(average)                   # calculating empirical queue length
        


max_queue_size = np.amax(q)                                  # max queue length
theoretical_queuelen = rho / (1 - rho)                       # finding theoretical queue length
print(statistics.median(q))                                  # Median of empirical queue length
print(statistics.mean(q))                                    # Mean of empirical queue length
print(theoretical_queuelen)
print(max_queue_size)
list_theoretical_queue_len = [theoretical_queuelen] * (len(empirical_queuelen))  #making list variable for
                                                                                 # theoretical queue length of size = runtime

t = np.arange(0, len(empirical_queuelen), dtype=int)
plt.scatter(t, empirical_queuelen)
plt.scatter(t, list_theoretical_queue_len)
plt.show()

