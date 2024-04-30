import numpy as np

def vectorLength(_vector):
    total = (_vector[0]**2)+(_vector[1]**2)+(_vector[2]**2)
    return np.sqrt(total)

def vectorUnit(_vector):
    return _vector/vectorLength(_vector)

def projectionLength(_vectorA, _vectorB):
    vp=_vectorA*_vectorB
    return vectorLength(vp)/vectorLength(_vectorB)

def projectionVector(_vectorA, _vectorB):
    return vectorUnit(_vectorB)*projectionLength(_vectorA,_vectorB)
