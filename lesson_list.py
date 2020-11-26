r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 100 in r:
    print('exist')
else:print('false')

r.sort()
print(r)
r.sort(reverse=True)
print(r)