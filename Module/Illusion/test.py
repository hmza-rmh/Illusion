from script import v as v
from random import shuffle
from random import randint as ri
import os

cl = v.const_list
cs = v.const_string
INfile = b'             <E>        \n<6>'
var = INfile.decode().split()
for e in var: print(e[1:-1])

def zReplace(x, l1, l2):
    for s, y in zip(l1, l2): x.replace(s, y)
    return x

def getkey(file):
    lst = []
    if file:
        with open(file, 'rb') as f:
            content = f.read().decode().split()
        for e in content: lst.append(e[1:-1])
    return lst

def genkey(el, file=False):
    shuffle(el)
    res, ext = ''.join(c for c in el), '.txt'
    if file:
        format = f'{res}' + ext
        if os.path.exists(format):
            for i in range(1000):
                FORMAT, format = f'{res}' + str(i) + ext, ''
                if not os.path.exists(FORMAT): break
        fFormat = FORMAT if not format else format
        with open(fFormat, 'w') as f:
            for c in el:
                f.write(f"{ri(0, 99)*' '}<{c}>\n")
    return res


print(genkey(list(v.const_string), True))
print(getkey('jsOKIUvkruoaPSwfimJyFdpGLnqA.txt'))
