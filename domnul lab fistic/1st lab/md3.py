import itertools

arr = list(input("enter: ").split())

perm = list(itertools.permutations(arr))
index = perm.index(tuple(arr))
next = perm[index + 1] if index + 1 < len(perm) else perm[0]

print(' '.join(next))
