import numpy as np
import vector_projection_calc as vpc

a = np.array([float(x) for x in input("Please enter the vector which will be on (comma seperated): ").split(",")])
b = np.array([float(x) for x in input("Please enter the vector which will be down (comma seperated): ").split(",")])

#Example result
#a=(2,3,0) /b=(0,-2,5) -> result = (0, -0.4137931, 1.03448276)

result= vpc.projectionVector(a,b)
print(result)