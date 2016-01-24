import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(1104758)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(x**2)*7*(x**0), (x,0, 0.4))
    return ans

def my_solution():
    A = np.array( [[3,1], [1,2]] )
    b = np.array([9,8])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1104758
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
