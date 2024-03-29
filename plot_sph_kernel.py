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

fig, ax = plt.subplots(1,2,figsize=(10,5))
ax[0].plot(q, f, c='grey')
ax[0].set_ylim([0,1.1])
ax[0].set_xlim([-2,2])
ax[0].set_ylabel(r'$f(q)$')
ax[0].set_xlabel(r'$q$')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()

# Now lets plot this kernel on a 2D plot which also contains other particles
# initialise a set of particles
p1 = [0,0]
p2 = [0.5,0.5]
p3 = [-1.3,1.4]
p4 = [-0.3,-1.7]
p5 = [-1.5,-1.0]
p6 = [-0.5, -0.7]
p7 = [2.3,1.2]
p8 = [-2.5,1.0]
p9 = [-2.3,-1.7]
p10 = [1.7,-2.7]
p11 = [1.2,2.7]
particles = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]
# generate meshgrid of the kernel function
XX, YY = np.meshgrid(q,q)
QQ = (XX*XX + YY*YY)**0.5
FF = np.zeros([len(q),len(q)])
# fill in values for 0 < q <= 1
FF[QQ <= 1] = 1 - 1.5*QQ[QQ<=1]**2 + 0.75*QQ[QQ<=1]**3
# fill in values for 1 < q <= 2
FF[QQ > 1] = 0.25*(2- QQ[QQ>1])**3
# fill in values for q > 2
FF[QQ >= 2] = 0
# plot the 2D kernel function
ax[1].contourf(XX, YY, FF, cmap='binary', levels=1000)
# plot the particle locations
for p in particles:
    ax[1].scatter(p[0],p[1], c='black', edgecolors='white', s=100)
# plot outline around outer edge of kernel
circle = plt.Circle((0,0), 2.0, fill=False, color='black', linestyle=':')
ax[1].add_patch(circle)
ax[1].set_ylim([-3,3])
ax[1].set_xlim([-3,3])
plt.gca().set_aspect('equal', adjustable='box')
ax[1].set_xticks([])
ax[1].set_yticks([])
# remove bounding box
ax[1].axis('off')
plt.tight_layout()
plt.savefig(os.path.join(out_path, 'sphKernel.png'))
plt.show()
