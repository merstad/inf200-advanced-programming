import random
import matplotlib.pyplot as plt
import numpy as np

random.seed(12345678)
results = []

for _ in range(1000):
    steps = 0
    position = 0
    while position < 25:
        position += random.randint(1, 6)
        if position == 1:
            position = 12
        elif position == 13:
            position = 22
        elif position == 14:
            position = 3
        elif position == 20:
            position = 8
        steps += 1
    results.append(steps)

print(f'Shortest game duration: {min(results):4d}')
print(f'Mean game duration    : {np.mean(results):6.1f} ± {np.std(results):.1f}')
print(f'Longest game duration : {max(results):4d}')

hv, hb = np.histogram(results, bins=np.arange(0, max(results)))
plt.step(hb[:-1], hv)
plt.show()
