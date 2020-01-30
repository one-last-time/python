import numpy as np

x=np.arange(1,10)
print(x)
x=np.reshape(x,(9,1))
print(x)
print(x.shape)

print(x[1,0])

