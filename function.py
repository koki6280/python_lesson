def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return  'green pepper'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)

def add_num(a: int, b: int) -> int:
    return a + b

r = add_num('a', 'b')
print(r)

def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink =', drink)
    print('dessert =', dessert)

menu(entree='beef', drink='beer', dessert='ice')

def menu2(entree='beef', drink='whine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)
menu2('sushi', drink='cola')

print('###########')

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)
say_something('Hi!', 'Mike', 'Nance')

# t = ('Mike', 'Nancy')
# say_something('Hi!', *t)

def menu3(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu3('banana', 'apple', 'orange', entree='beef', drink='coffee')

'''
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu3(**d)
'''




