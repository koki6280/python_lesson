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




