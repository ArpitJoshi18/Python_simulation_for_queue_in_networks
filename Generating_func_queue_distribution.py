import matplotlib.pyplot as plt
import numpy as np
run_time = 10000000
max_a = 44
max_s = 100
avg_a = (max_a-1)/2
avg_s = (max_s-1)/2
a_squared = (max_a-1)*(2*(max_a-1)+1)/6
s_squared = (max_s-1)*(2*(max_s-1)+1)/6
theoretical_ubound_q = np.full(run_time, (a_squared-2*avg_a*avg_s+s_squared)/(2*(avg_s-avg_a)))
q = np.zeros(run_time, dtype=int)
empirical_average_q = np.zeros(run_time)
for i in range(len(q)):
    a = np.random.randint(0, max_a)
    s = np.random.randint(0, max_s)
    if i < len(q)-1:
        q[i+1] = max(q[i] + a - s, 0)
        empirical_average_q[i+1] = ((i+1)*empirical_average_q[i]+q[i+1])/(i+2)
t = np.arange(0, run_time,dtype=int)
plt.scatter(t, empirical_average_q)
plt.scatter(t, theoretical_ubound_q)
plt.xlabel("time")
plt.ylabel("average queue size")
plt.show()
