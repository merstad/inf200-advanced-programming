import random
import matplotlib.pyplot as plt
import numpy as np

res = []

for _ in range(1000):
    s = 0
    p = 0
    while p < 25:
        p += random.randint(1, 6)
        if p == 1:
            p = 12
        elif p == 13:
            p = 22
        elif p == 14:
            p = 3
        elif p == 20:
            p = 8
        s += 1
    res.append(s)

print(f'Shortest game duration: {min(res):4d}')
print(f'Mean game duration    : {np.mean(res):6.1f} ± {np.std(res):.1f}')
print(f'Longest game duration : {max(res):4d}')

hv, hb = np.histogram(res, bins=np.arange(0, max(res)))
plt.step(hb[:-1], hv)
plt.show()
