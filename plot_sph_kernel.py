import os
import numpy as np
import matplotlib.pyplot as plt

out_path = '../figures/chap3'

# distance from central particle
q = np.arange(-2,2.01,0.01)
# kernel function
f = np.zeros(401)
# fill in values for 0 < q <= 1
f[np.abs(q)<=1] = 1 - 1.5*q[np.abs(q)<1]**2 + 0.75*np.abs(q[np.abs(q)<1])**3
# fill in values for 1 < q <= 2
f[np.abs(q)>1] = 0.25*(2- np.abs(q[np.abs(q)>1]))**3

plt.plot(f, c='grey')
plt.xticks([])
plt.ylim([0,1.1])
plt.tight_layout()
plt.savefig(os.path.join(out_path, 'sphKernel.png'))
plt.show()
