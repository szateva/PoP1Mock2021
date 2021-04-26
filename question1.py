# 13021326

""" the function compares two lists element by element and creates a new list containing
the largest of the two elements compared. """

def fun(L1, L2):
    if L1==[] and L2==[]:
        return []
    else:
        if L1[0] > L2[0]:
            return [L1[0]]+fun(L1[1:], L2[1:])
        else:
            return [L2[0]]+fun(L1[1:], L2[1:])


a = [5, 7, 9, 2]
b = [2, 3, 6, 8]

print(fun(a, b))