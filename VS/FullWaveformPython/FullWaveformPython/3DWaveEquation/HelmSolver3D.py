import numpy as np
import scipy as sp
class HelmSolver3D:
    """This class solves for 3D helm equation in a sparsifying techinique"""

    def HelmSolve(helm, f, m, b, o , d, n , nb, beta, l):
        N= 0
        w=0.0
        N= n[0]*n[1]*n[2]
        w= 2*np.pi*f
        p1 = np.array([[1- np.power((beta/w)*1j* np.linspace(1,0, nb[0]),l)], [np.ones(n[0]-2*nb[0])],[1-np.power((beta/w)*1j*np.linspace(0,1, nb[0]),l)]])
        p2 = np.array([[1- np.power((beta/w)*1j* np.linspace(1,0, nb[1]),l)], [np.ones(n[1]-2*nb[1])], [1-np.power((beta/w)*1j*np.linspace(0,1, nb[1]),l)]])
        p1 = np.array([[1- np.power((beta/w)*1j* np.linspace(1,0, nb[2]),l)], [np.ones(n[2]-2*nb[2])], [1-np.power((beta/w)*1j*np.linspace(0,1, nb[2]),l)]])
        return 
