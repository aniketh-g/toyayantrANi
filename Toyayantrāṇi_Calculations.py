import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
#Units
mm_2_aGgula = 1/17.65 #1mm equals 17.65 aṅgula-s
hour_2_nADI = 24/60
#Constants
g = 9.80665 * 1000 * mm_2_aGgula / ((1/3600) * hour_2_nADI)**2 #Acceleration due to gravity in aṅgula/nāḍī^2
#Parameters
ghaTikAGgula = 1 #number of aṅgula-s fallen in 1 nāḍī
r0 = 0.5*mm_2_aGgula #hole radius in mm
T = 5 #Total time of operation in nāḍī-s
#Equation of container curve
def h(r, r0):
    return (ghaTikAGgula**2/(2*g))*((r/r0)**4-1) #v = T*ghaTikAGgula/T
def r(h, r0):
    return r0*(((h/((ghaTikAGgula**2/(2*g))))+1)**0.25) #v = T*ghaTikAGgula/T

def plotshape(r0, ghaTikAGgula, T, c='b', lines=True, box=False):
    ys = list(np.linspace(0, T*ghaTikAGgula, T))
    plt.plot([r(h, r0) for h in ys], ys, '.-', color=c, label="ghaṭīkāṅgula = %s aṅgula"  %ghaTikAGgula)
    
    if lines:
        [plt.hlines(y=h, xmin=0, xmax=r(h, r0), color=c) for h in ys]
    
    if box:
        plt.hlines(0, xmin=0, xmax=r(T*ghaTikAGgula, r0), color=c)
        plt.vlines(r(ghaTikAGgula*T, r0), ymin=0, ymax=T*ghaTikAGgula, color=c)
        plt.hlines(ghaTikAGgula*T, xmin=0, xmax=r(T*ghaTikAGgula, r0), color=c)
        plt.vlines(0, ymin=0, ymax=T*ghaTikAGgula, color=c)

def mouldvol(r0, ghaTikAGgula, T):
    return ghaTikAGgula*T*4*(r(ghaTikAGgula*T, r0)**2)

# ghaTikAGgulas = list(np.linspace(0, 4, 20))
# for r0 in [0.5, 1, 1.5]:
#     r1 = r0*mm_2_aGgula
#     plt.plot(ghaTikAGgulas, [mouldvol(r1, gh, T) for gh in ghaTikAGgulas], ".-", label="r0 = %s mm" %r0)

# plt.legend()
# plt.show()

# r0s = list(np.linspace(0.1*mm_2_aGgula, 4*mm_2_aGgula, 20))
# for gh in [1, 2, 3]:
#     plt.plot(r0s, [mouldvol(r1, gh, T) for r1 in r0s], ".-", label="ghaṭikāṅgula = %s aṅgula" %gh)

color = iter(cm.rainbow(np.linspace(0, 1, 10)))
for ghaTikAGgula in [1, 2, 3]:
    c = next(color)
    plotshape(r0, ghaTikAGgula, T, c, lines=False, box=True)

plt.legend()
plt.show()