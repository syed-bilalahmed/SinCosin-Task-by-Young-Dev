import numpy as np
import matplotlib.pyplot as plt

# Generate an array of values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)

# Calculate sine and cosine for each x value
y_sine = np.sin(x)
y_cosine = np.cos(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sine, label='Sine', color='blue')     # Sine curve
plt.plot(x, y_cosine, label='Cosine', color='orange')  # Cosine curve

# Add title and labels
plt.title('Sine and Cosine Graphs')
plt.xlabel('Angle (radians)')
plt.ylabel('Value')
plt.axhline(0, color='black', lw=0.5, ls='--')  # x-axis
plt.axvline(0, color='red', lw=0.5, ls='--')  # y-axis
plt.grid()
plt.legend()  # Show legend

# Show the plot
plt.show()
