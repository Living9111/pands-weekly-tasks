import numpy as np
import matplotlib.pyplot as plt
minsalary = 20000
maxsalary = 80000
numberofEntries = 100
ages = np.random.randint(low = 21, high = 65, size = numberofEntries)
np.random.seed(1)
salaries= np.random.randint(minsalary, maxsalary, numberofEntries)
plt. scatter (ages,salaries)
plt.show()