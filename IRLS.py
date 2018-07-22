import numpy as np
import numpy.linalg as la

# regularization to improve stability
regLambda=1e-6

def weightedLS(A,b,w):
    # find a weighted least squares solution to Ax=b
    # weights are given by w
    n=w.size
    s=w+regLambda*np.ones(n)
    S=np.diag(s)
    L=A.dot(S).dot(A.T)
    p=la.solve(L,b)
    q=S.dot(A.T).dot(p)
    return q

def runIRLS(A,b,numIter):
    # run the IRLS algorithm for minimizing ||x||_1 over Ax=b
    # the number of iterations is given by numIter
    n=A.shape[1]
    for i in range(numIter+1):
        if i==0:
            w=np.ones(n)
        else:
            w=np.absolute(x)
        q=weightedLS(A,b,w)
        x=q
    return x
    
    
def runPhysarumDyn(A,b,stepSize,numIter):
    # run Physarum Dynamics for minimizing ||x||_1 over Ax=b
    # the stepSize \in (0,1) determines the step size
    # the number of iterations is given by numIter
    n=A.shape[1]
    w=np.ones(n)
    x=weightedLS(A,b,w)
    for i in range(numIter+1):
        q=weightedLS(A,b,w)
        x=(1-stepSize)*x+stepSize*q
        w=(1-stepSize)*w+stepSize*np.absolute(q)
    return x
            


    