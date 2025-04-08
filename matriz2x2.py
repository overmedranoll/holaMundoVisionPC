
import matplotlib.pyplot as plt
import numpy as np

I = np.array([[0, 250], [250,0]])

plt.imshow(I, cmap='gray', vmin=0, vmax=255)
plt.show()