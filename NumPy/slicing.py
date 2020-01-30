import numpy as np
x= np.arange(20).reshape((4,5))
print(x)

print(x[1:,:3])

print(x)
z= np.diag(x,k=0)
print(z)
z=np.diag(x,k=1)
print(z)

z= x[1:3,2:4].copy()
print(z)

z[0,0]=-1
print(z)
indecies=np.array([2,3])

z=x[indecies,:]
print(z)
z=x[:,indecies]
print(z)

z=x[indecies,indecies]
print('herre',z)


# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(1,26,1).reshape(5,5)
print(X)

# Use Boolean indexing to pick out only the odd numbers in the array
Y =X[X%2==1] 
print(Y)

X=np.arange(0,6,1).reshape(2,3)
print(X.mean())
