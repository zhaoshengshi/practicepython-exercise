
import random

def list_gen():
    li = []
    size = random.randint(1, 100)
    for i in range(size):
        li.append(random.randint(1, 1000))
    return li

a = list_gen()
b = list_gen()

print('a:', a)
print('b:', b)

print('a&b:', list(set(a) & set(b)))
