import numpy as np
import tensorflow
import torch as pt

a=np.array([[1,2,1],[1,2,1]])
b=np.array([[1,2],[2,1],[1,2]])
a=a.dot(b)
print(a)