import HelmSolver3D as h3d
import numpy as np1
helm= h3d.HelmSolver3D()
f=5
m= np1.ones(46656)
o=np1.array([-100 ,-100 ,-100])
d=np1.array([20, 20, 20])
n= np1.array([36, 36, 36])
nb=np1.array([5,5,5])
helm.HelmSolve( 5,m,m,o,d,n,nb,100,2)