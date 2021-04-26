# 13021326

def apply_functions(f, g, L):
    M = []
    for i in L:
        if i >= 0:
            M.append(f(i))
        else:
            M.append(g(i))
    return M

# Indicative test cases:
def double(x):
    return 2*x
def square(x):
    return x*x

assert apply_functions(double, square, [1,-6,-3,5]) == [2,36,9,10]
print("must be True")

#abs is the standard function returning absolute value
assert apply_functions(double, abs, [1,-6,-3,5]) == [2,6,3,10]
print("must be True")