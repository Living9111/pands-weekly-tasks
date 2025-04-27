import matplotlib.pyplot as plt
import numpy as np
minsalary = 20000
maxsalary = 80000
numberoofEntries = 100
np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, numberoofEntries)
plt.hist(salaries)
plt.show()