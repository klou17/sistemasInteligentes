import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import pairwise_distances

Y = np.array([
    [5, 8, 4],
    [7, 2, 1],
    [3, 9, 0],])


plt.axis([0, 14, 0, 14])
plt.plot((pairwise_distances(Y, metric='manhattan')), '.-', markevery=(0, 1))
plt.show()



