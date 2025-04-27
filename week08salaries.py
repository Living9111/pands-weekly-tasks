# question 1 to 4, week 08 Lab

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
salariesPlus = salaries + 5000 
np.random.seed(1) 
salariesmult = salaries * 1.05
print('salaries multiplied by 5 percent:',salariesmult)
print('salaries:',salaries)
print('salaries added by 5000:',salariesPlus)

