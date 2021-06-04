import matplotlib.pyplot as plt
import numpy as np


my_data = np.array([65, 24, 84, 78])
my_students = ["Mikayla", "Andrew", "Ayanda", "Lihle"]

plt.pie(my_data, labels=my_students)
plt.show()