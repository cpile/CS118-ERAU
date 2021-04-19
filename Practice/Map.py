
def even(k):
    return k % 2 == 0


def odd(k):
    return not k % 2 == 0


def my_filter(f, it):
    return [i for i in it if f(i)]


text = "1,2,3,4,5,6,7,8,9,10"

x = list(filter(even, map(int, text.split(","))))
y = list(filter(odd, map(int, text.split(","))))
y = list(my_filter(odd, map(int, text.split(","))))


# n = sum(map(int, text.split(",")))
print(x)
print(y)

