import copy


def minPathSum(tree, m):

    backup = copy.deepcopy(tree)

    for i in range(m - 1, -1, -1):
        for j in range(i + 1):
            if tree[i + 1][j] < tree[i + 1][j + 1]:
                tree[i][j] += tree[i + 1][j]
            else:
                tree[i][j] += tree[i + 1][j + 1]

    list = []

    t = 0
    list.append(0)

    for p in range(1, m+1):
        if tree[p][t] < tree[p][t+1]:
            list.append(t)
        else:
            t += 1
            list.append(t)

    wynik = []

    for p in range(m+1):
        wynik.append(backup[p][list[p]])

    return tree[0][0], list, wynik


data = []

with open("medium.txt") as f:
    for line in f:
        numbers_str = line.split()
        numbers = [int(x) for x in numbers_str]
        data.append(numbers)


wynik, listindx, sciezka = minPathSum(data, len(data)-1)

print(wynik, listindx)
print(sciezka)


