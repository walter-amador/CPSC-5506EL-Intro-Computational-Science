import math

print("\nEquation")
a = (3*4)/(2**2 + 4/2)
print(a)

print("\nSquare root")
b = math.sqrt(4)
print(b)

print("\nSin")
c = math.sin(math.pi/2)
print(c)

print("\nExponential and logarithm")
d = math.exp(math.log(10))
print(d)

print("\nExponential")
e = math.exp(3/4)
print(e)

print("\nInfinity")
f = 1/math.inf
print(f)

print("\nInfinity")
g = math.inf * 2
print(g)

print("\nComplex number")
# 2 + 5j
h = complex(2, 5)
print(h)

print("\nComplex number")
# 2 + 5j
i = (2 + 5j)
print(i)

print("\nData types using type function")
print(type(1234))

print(type(3.14))

print(type(3+4j))

print(type([1, 2, 3, 4]))

print(type("Hello world"))

print(type(True))

print("\nLength of the text")
text = "Hello world"
length = len(text)
print(length)

upper = text.upper()
print("Upper case", upper)

count_l = text.count("l")
print(count_l)

print("Replacing string")
replace = text.replace("world", "Python")
print(replace)

list_1 = [1, 2, 3]
print(list_1)
