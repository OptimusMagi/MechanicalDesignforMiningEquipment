# For a simpler design project, you can simulate a mechanical system behavior or create a basic structural analysis.
# 1. Set up the Project: Create a simulation of a basic mechanical system (e.g., spring-mass system).
# 2. Install Required Libraries:
# 3.  Run 'bash' commands and scripts in Linux and Mac environments.
# In terminal:
# pip install numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 1  # kg
spring_constant = 10  # N/m
time = np.linspace(0, 10, 100)  # seconds

# Simulating oscillation
displacement = np.sin(np.sqrt(spring_constant/mass) * time)

# Plotting the results
plt.plot(time, displacement)
plt.title('Spring-Mass Oscillation')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid()
plt.show()

#4. Run: This code simulates and visualizes a spring-mass oscillation

