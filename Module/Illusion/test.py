from script import *
from string import ascii_lowercase as acl, ascii_uppercase as acu, digits as dg

Alphabet = acl+acu+dg+'+/'
key = getkey('key.key')
print(key)
print()
print(v.const_list)
print()
for x, y in zip(key, v.const_list):
    print(f'{x} : {y}')
print()


print(Alphabet)
print()

mybin = turn_binary(Alphabet, 'to')
print(mybin)
print()
compressed = comp(mybin)
print(compressed)
print()
bh = enc(compressed, key)
print(bh)

o = turn_binary(decomp(dec(bh, key)), 'from')
print()
print(o)
