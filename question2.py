# 13021326

def replace(t):
    changed = list(t)
    for i in range(0, len(t)):
        if t[i]<0:
            changed[i] = -t[i]
        else:
            changed[i] = t[i]
    return changed

a = (-5, 0, 3, -2)
print(replace(a))

""" tuples are immutable, hence the assignment changed[i] = -t[i] will crash the code. One potential solution
 is to convert the tuple to a list and manipulate this newly created list, then convert it to a new tuple and 
 return the new tuple.
 range(1, len(t)) is wrong. In Python the indexing start with 0, so the code in the present format 
 will only look at the tuple between the second and last elements in the tuple. 
 To fix this the code range(0, len(t)) should be used"""