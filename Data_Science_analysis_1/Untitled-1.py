


def Solution(A):
    d = []
    for i in A:
        if i not in d:
            d.append(i)
        else:
            print(i)

Solution('docality')
