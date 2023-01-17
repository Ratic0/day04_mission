# 8.1
e2f ={'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
print(f'8.1 : {e2f}')
print(f"8.2 : {e2f['walrus']}")

f2e = {}

for e2f_key, contents in e2f.items() :
    f2e[contents] = e2f_key
    if 'chien' in contents :
        print(f'8.4 : {e2f_key}')

print(f'8.3v1 : {f2e}')

q = { a:b for b, a in e2f.items() }

print(f'8.3v2 : {q}')

print(f'8.5 : {list(e2f.keys())}')

# 8.6
life = {'animals' :
            {'cat' : 'Henri','octopi' : 'Grumpy', 'emus' : 'Lucy'}
        ,
        'plants' : {}
        ,
        'others' : {}
        }
# 8.7
print(f'8.7 : {list(life.keys())}')
# 8.8
print(f"8.8 : {life['animals']}")
# 8.9
print(f"8.9 : {life['animals']['cat']}")





