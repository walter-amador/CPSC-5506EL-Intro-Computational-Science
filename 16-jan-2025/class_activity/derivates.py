
# Calculate derivative of arcsin(2x)
import sympy as sp

x = sp.symbols('x')
f = sp.asin(2*x)

f_prime = sp.diff(f, x)

print(f_prime)
