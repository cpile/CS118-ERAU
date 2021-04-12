import random

N = 1000


def foo(a): # a is of type tuple
    return a[1]


d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(N):
    v = random.randint(1, 6)
    d[v] += 1
assert (N == sum(d.values()))
x = list(d.items())
x.sort(reverse=True, key=foo)
print(x)




