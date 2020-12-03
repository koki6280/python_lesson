print('hello')
print("I don't know")
print('I don\'t know')
print('say "I don\'t know')
print("say \"I don't know\"")

print('hello. \nHow are you?')
print(r'C:\name\name')

print("##########")
print("""\
line1
line2
line3\
""")
print("##########")

print('Hi.' * 3 + 'Mike.')
print('Py''thon')
prefix = 'Py'
print(prefix + 'thon')

s = ('aaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbb')

print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
word = 'j' + word[1:]
print(word)
print('##############')
s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)
print('##############')
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))
print('##############')

# import lesson_package.utils
# from lesson_package.touls import utils

# from lesson_package.utils import say_twice

# r = utils.say_twice('hello')
# print(r)

# from lesson_package.talk import human
# from lesson_package.talk import animal
# from  lesson_package.talk import *

# print(animal.sing())
# print(animal.cry())

# print(human.sing())
# print(human.cry())

try:
    from lesson_package import utols
except ImportError:
    from lesson_package.touls import utils

utils.say_twice('word')

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

print(sorted(ranking, key=ranking.get, reverse=True))

s = "fojoeirnnknsjhebdfbvnffaacksk"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

from collections import defaultdict
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)
print(d['f'])







