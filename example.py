from IRLS import *

# Simple l_1 minimization problem
# min ||x||_1    s.t. x_1 + 2*x_2=1
# the optimal solution is x=(0, 0.5)
A=np.array([[1,2]])
b=np.array([1])
w=np.array([1,1])


# Run the IRLS algorithm for 10 steps
print(runIRLS(A,b,10))

#Run the Physarum dynamics for 10 steps, with step-size 0.3
print(runPhysarumDyn(A,b,0.3,10))