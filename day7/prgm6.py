import numpy as np
expenses = np.array([20, 60, 5, 80, 45, 90])
modified_expenses = np.where(expenses < 50, 0, expenses)
print(modified_expenses)  