import numpy as np

num = np.random.default_rng()
list = num.random(10)
print(list)
print(np.mean(list))
print(np.median(list))
print(np.std(list))