import numpy as np

a = np.zeros((4, 4), dtype=int)

print(a)
# [[0 0 0 0]
# [0 0 0 0]
# [0 0 0 0]
# [0 0 0 0]]
print(a.shape)  # (4, 4)

b = np.reshape(a, (2, 8))
print(b)
# [[0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0]]
