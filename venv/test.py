import numpy as np
import matplotlib.pyplot as plt

from scipy import stats
x = [1,1,4,4]
y = [1,4,1,4]
np.average
print(np.mean(x))
x.append(np.mean(x))
y.append(np.mean(y))

data = np.column_stack((x, y))

fig, (ax1) = plt.subplots(
    nrows=1
)

ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
ax1.set_title('Scatter: $x$ versus $y$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')




plt.show()