import matplotlib.pyplot as plt
import numpy as np

for i in range(100):
    plt.plot(np.random.rand(100), linewidth = 1)

plt.title("Too much confusing")
plt.tight_layout()
plt.show()