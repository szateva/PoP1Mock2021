# 13021326

def trim_matrix(M):
    shortest = len(M[0])
    # print("the shortest is: ", shortest)
    for i in M:
        if len(i) < shortest:
            shortest = len(i)
            # print("new shortest is: ", shortest)

    for row in range(0, len(M)):
        for col in range(len(M[row])-1, shortest-1, -1):
            del M[row][col]

# Indicative test cases:
X = [[1,2,3],[12,13],[21,22,23,24]]
trim_matrix(X)
print(X)
assert X == [[1,2],[12,13],[21,22]]
X = [[1,2,3],[12,13,14]]
trim_matrix(X)
print(X)
assert X == [[1,2,3],[12,13,14]]
X = [[1,2,3],[12,13,14],[]]
trim_matrix(X)
print(X)
assert X == [[],[], []]