# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#for i in num_list:
#    print(i)

# for i in range(2, 10, 3):
#   print(i)

for _ in range(10):
    print('hello')


# for i, fruit in enumerate(['apple', 'banana', 'orange']):
#    print(i, fruit)

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
#   print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)
