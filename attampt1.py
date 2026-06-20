pip install numpy matplotlib.pyplot

import numpy as np
import matplotlib.pyplot as plt

Total_drivers = 1000
iterations = 40
learning_rate = 0.001

# Inital conditions
A_driver = 90/100*Total_drivers
B_driver = Total_driver - A_driver

avg_cost_inf = np.zeros(iterations)

def get_cost_A(A_driver):
  return 15 + 0.01*A_driver

def get_cost_B(B_driver):
  return 2 + 0.1*B_driver

for i in range(iterations):
  B_driver = Total_drivers - A_driver
  
  cost_A = get_cost_A(A_driver)
  cost_B = get_cost_B(B_driver)
  avg_cost = ( cost_A*A_driver + cost_B*B_driver ) / Total_drivers
  avg_cost_inf[i] = avg_cost
  
  frac_A = A_driver/Total_driver
  del_frac_A = learning_rate*frac_A*(avg_cost - cost_A)
  
  frac_A_upd = frac_A + del_frac_A
  A_driver = frac_A_upd * Total_drivers

t = np.linspace(1,iterations,iterations)
plt.figure()
plt.plot(t,avg_cost_inf)
plt.title("Evolution of traffic")
plt.xlabel("Time")
plt.ylabel("Average travel duration per day")
plt.show()

print("The average travel duration at traffic equilibrium is:",avg_cost_inf[iterations-1])
print("The travel duration through path A:",get_cost_A(A_driver))
print("The travel duration through path A:",get_cost_B(Total_drivers - A_driver))
