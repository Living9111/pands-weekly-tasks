#histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
import numpy as np
import matplotlib.pyplot as plt

# Generating some random data
data = np.random.normal(5, 2, 1000)

# Plotting the histogram
plt.hist(data, bins=25, density=True, alpha=0.6, color='blue', label='Data')

# Adding labels, title, and legend
plt.title("Histogram of Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend(loc='upper right')  # Add legend in the upper-right corner

plt.show()



# plot of the function  h(x)=x3 in the range 0 to 10, 
import numpy as np
import matplotlib.pyplot as plt

# Define the range and the function
x = np.linspace(0, 10, 100)  # Generate 100 points between 0 and 10
h_x = x**3  # Compute h(x) = x^3

# Plot the function
plt.plot(x, h_x, label="h(x) = x^3", color='red')

# Add labels, title, and legend
plt.title("Plot of h(x) = x^3")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.legend(loc='upper left')  # Add legend in the upper-left corner

# Show the plot
plt.grid(True)  # Add a grid for better visualization
plt.show()