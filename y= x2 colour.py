import numpy as np
import matplotlib.pyplot as plt
minsalary = 20000
maxsalary = 80000
numberofEntries = 100
np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, numberofEntries)

ages = np.random.randint(low= 21, high = 65, size = numberofEntries)

plt.scatter(ages, salaries)
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints
plt.plot(xpoints, ypoints, color= 'r')
plt.show()