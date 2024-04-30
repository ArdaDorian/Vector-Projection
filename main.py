import numpy as np
import vector_projection_calc as vpc

a = np.array([float(x) for x in input("Please enter the vector which will be on (comma seperated): ").split(",")])
b = np.array([float(x) for x in input("Please enter the vector which will be down (comma seperated): ").split(",")])

result= vpc.projectionVector(a,b)
print(result)