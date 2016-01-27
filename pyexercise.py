import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(1104758)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate(7 * (x**9) / (sy.exp(x**2)) , (x,0, np.inf))
    return ans

def my_solution():
    A = np.array( [[1,1,1,1,1,1,1,1,1,1],[2,2,1,0,1,1,0,0,0,0],[0,1,1,1,4,17,7,1,21,1],[1,0,1,1,12,6,28,20,11,3],[0,1,0,1,13,15,3,9,7,2],[1,0,1,1,9,14,16,32,10,10],[0,1,1,0,7,27,6,6,14,12],[0,1,0,0,13,21,8,13,5,7],[0,0,0,1,6,18,9,36,12,4],[1,0,1,1,3,17,9,19,5,40]] )
    b = np.array([45,13,333,506,286,601,464,400,555,689])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1104758
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
