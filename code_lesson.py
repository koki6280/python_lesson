x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

# a = 1
# b = 2

# if not a == b:
    # print('Not equal')

# if a != b:
    # print('Not equal')

# is_ok = True
is_ok = [1, 2, 3, 4]

# False 0, 0.0, '', [], (), {}, set()
if is_ok:
    print('OK!')
else:
    print('No!')

is_empty = None
# print(help(is_empty))
if is_empty is None:
    print('None!!!')

print(1 == True)
print(True is True)

# count = 0
# while count < 5:
    # print(count)
    # count += 1

'''
count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue
    print(count)
    count += 1
'''

count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')


while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')


