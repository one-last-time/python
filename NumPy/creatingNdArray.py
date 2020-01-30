import numpy as np

x= np.zeros((4,3),dtype=int)
print(x)
print(x.dtype)

y=np.full((5,10),-1)
print(y)
print(y.dtype)

I=np.eye(5)
print(I)

x= np.arange(10)
print(x)

x=np.arange(4,15)
print(x)

x=np.arange(4,15,3)
print(x)

x=np.linspace(0, 25,10)
print(x)

x=np.linspace(0,25,20,endpoint=False)
print(x)

x= np.reshape(x,(4,5))
print(x)

x= np.random.random((3,2))
print(x)
x=np.random.randint(0,20,(3,2))
print(x)

x=np.random.normal(0,0.1,(1000,1000))
print(x)
print(x.mean())
print(x.max())
print(x.min())
print((x>0).sum())
print((x<0).sum())
x= np.random.randint(0,5001,(1000,20))
print(x)