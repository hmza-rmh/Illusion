#!/usr/bin/junk
#import random, string#, json

"""
def x(element):
    n = 0
    res = ''
    v = element[:1]
    for c in element:
        for k in v:
            if int(c) == 0 and c + k == '00':
                n += 1
                res += str(n)
            else:
                res += str(c)
    return res
"""
"""
def x(element):
    n = 0
    f = 0
    res = ''
    calc = ''
    lent = len(element)
    while True:
        if str(element[f]) + str(element[f+1]) == '00':
            n+=1
            if str(element[f]) + str(element[f+1]) != '00':
                res += str(n)
            else:
                pass
        else:
            res += str(element[f])
        f+=1
        if f > lent: break
"""
"""
def comp(x):
    x, f = x.replace("1", "x"), ''
    for i in range(len(x) - 1):
        if x[i] == '0' and x[i + 1] == '0': f += x[i]
    f+='0'
    h = eval('+'.join(c for c in f.replace("0", '1')))
    return x.replace(f, str(h)).replace("x", "1")
""" 
"""
def decomp(x):
    for c in x:
        if int(c) > 1: n, s = int(c), ''
    for i in range(n): s += '0'
    return x.replace(str(n), s)
"""
"""
Alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + '+/'
strc = ''.encode()
for c in Alphabet:
    strc += f'"{c}":"",\n'.encode()
strc = strc[:-2]
strc = '{\n'.encode()+strc+'\n}'.encode()
with open('data.json', 'wb') as f:
    f.write(strc)
    print(strc)
"""
"""
Alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + '+/'
z=[]

def addh(el):
    with open('z.txt', 'a') as f:
        f.write(el)

def geth():
    with open('z.txt', 'r') as f:
        return f.read()

def p():
    while True:
        x = random.choice(Alphabet)
        if x in list(geth()): pass
        else:
            print(x)
            addh(x)
            break
"""
"""
def enc(x):
    
    if x[:2] == '11':
        marker = r'\hx'
        x = x[1:]
        if x[-1] == '1': x = '2' + x[1:-1]
    elif x[:2] != '11':
        marker = r'\hz'
        if x[-1] == '1': x = '2' + x[1:-1]
    return marker+x
    
def dec(x):
    if x[:4] == r'\hx2': x = '11' + x[4:] + '1'
    elif x[:4] == r'\hx1': x = '1' + x[3:]
    elif x[:4] == r'\hz2': x = '1' + x[4:] + '1'
    elif x[:4] == r'\hz1': x = x[3:]
    return x
"""
"""
def enc(x):
    l = split(x)
    nl = []
    for c in l:
        if c[:2] == '11':
            marker = r'\hx'
            if c[-1] == '1': nl.append(marker + '2' + c[2:-1])
            elif c[-1] == '0': nl.append(marker + '1' + c[2:-1] + '0')
            else: nl.append(marker + c[1:])
        elif c[:2] != '11':
            marker = r'\hz'
            if c[-1] == '1': nl.append(marker + '2' + c[1:-1])
            elif c[-1] == '0': nl.append(marker + '1' + c[1:-1] + '0')
            else: nl.append(marker + c)
    return join(nl)
    
def dec(x):
    l = split(x)
    nl = []
    for c in l:
        if c[:4] == r'\hx2': nl.append('11' + c[4:] + '1')
        elif c[:4] == r'\hx1': nl.append( '1' + c[3:])
        elif c[:4] == r'\hz2': nl.append('1' + c[4:] + '1')
        elif c[:4] == r'\hz1': nl.append(c[3:])
    return join(nl)
"""
"""
#./usr/bin/junk
import random, string#, json
"""
"""
def x(element):
    n = 0
    res = ''
    v = element[:1]
    for c in element:
        for k in v:
            if int(c) == 0 and c + k == '00':
                n += 1
                res += str(n)
            else:
                res += str(c)
    return res
"""
"""
def x(element):
    n = 0
    f = 0
    res = ''
    calc = ''
    lent = len(element)
    while True:
        if str(element[f]) + str(element[f+1]) == '00':
            n+=1
            if str(element[f]) + str(element[f+1]) != '00':
                res += str(n)
            else:
                pass
        else:
            res += str(element[f])
        f+=1
        if f > lent: break
"""
"""
def comp(x):
    x, f = x.replace("1", "x"), ''
    for i in range(len(x) - 1):
        if x[i] == '0' and x[i + 1] == '0': f += x[i]
    f+='0'
    h = eval('+'.join(c for c in f.replace("0", '1')))
    return x.replace(f, str(h)).replace("x", "1")
""" 
"""
def decomp(x):
    for c in x:
        if int(c) > 1: n, s = int(c), ''
    for i in range(n): s += '0'
    return x.replace(str(n), s)
"""
"""
Alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + '+/'
strc = ''.encode()
for c in Alphabet:
    strc += f'"{c}":"",\n'.encode()
strc = strc[:-2]
strc = '{\n'.encode()+strc+'\n}'.encode()
with open('data.json', 'wb') as f:
    f.write(strc)
    print(strc)
"""""" 

Alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + '+/'
z=[]

def addh(el):
    with open('z.txt', 'a') as f:
        f.write(el)

def geth():
    with open('z.txt', 'r') as f:
        return f.read()

def p():
    while True:
        x = random.choice(Alphabet)
        if x in list(geth()): pass
        else:
            print(x)
            addh(x)
            break
"""""" 
strng = '\n'
byts = strng.encode()
chr = '\ '
print(repr(strng[:-1]), repr(chr), repr(byts[:-1]))
"""
"""
def enc(x):
    l = split(x)
    nl = []
    for c in l:
        if c[:2] == '11':
            marker = r'\hx'
            c = c[1:]
            if c[-1] == '1': nl.append(marker + '2' + c[1:-1])
            elif c[-1] == '0': nl.append(marker + '1' + c[1:-1] + '0')
            else: nl.append(marker + c[1:])
        elif c[:2] != '11':
            marker = r'\hz'
            if c[-1] == '1': nl.append(marker + '2' + c[1:-1])
            elif c[-1] == '0': nl.append(marker + '1' + c[1:-1] + '0')
            else: nl.append(marker + c)
    return join(nl)
    
def dec(x):
    l = split(x)
    nl = []
    for c in l:
        if c[:4] == r'\hx2': nl.append('11' + c[4:] + '1')
        elif c[:4] == r'\hx1': nl.append( '1' + c[3:])
        elif c[:4] == r'\hz2': nl.append('1' + c[4:] + '1')
        elif c[:4] == r'\hz1': nl.append(c[3:])
    return join(nl)
"""
"""
def enc(x):
    l = x.split()
    nl = []
    for c in l:
        if c[:2] == '11':
            marker = 'x'
            if c[-1] == '1': nl.append(marker + '2' + c[2:-1])
            elif c[-1] == '0': nl.append(marker + '1' + c[2:-1] + '0')
            else: nl.append(marker + c[1:])
        elif c[:2] != '11':
            marker = 'z'
            if c[-1] == '1': nl.append(marker + '2' + c[1:-1])
            elif c[-1] == '0': nl.append(marker + '1' + c[1:-1] + '0')
            else: nl.append(marker + c)
    return ''.join(nl)
    
def dec(x):
    l = x.replace('x', 'hx').replace('z', 'hz').split('h')
    nl = []
    for c in l:
        if c[:2] == 'x2': nl.append('11' + c[2:] + '1')
        elif c[:2] == 'x1': nl.append( '1' + c[1:])
        elif c[:2] == 'z2': nl.append('1' + c[2:] + '1')
        elif c[:2] == 'z1': nl.append(c[1:])
    return ' '.join([c for c in nl])
"""
"""
import json, string

def view(el):
    return "-----------------------------------------\n" + repr(el) + "\n-----------------------------------------"
def turn_binary(element, direction):
    if direction.lower() == 'to': return ' '.join(bin(ord(se))[2:] for se in element)
    elif direction.lower() == 'from': return ''.join(chr(int(se, 2)) for se in element.split())
    else: raise Exception("Please choose a valid direction for the string.(From/To)")

def comp(x):
    x = x.replace("1", "x")
    parts = x.split('z')
    result = []
    for part in parts:
        count = 0
        new_part = ''
        i = 0
        while i < len(part):
            if part[i] == '0' and i + 1 < len(part) and part[i + 1] == '0':
                count = 0
                while i < len(part) and part[i] == '0':
                    count += 1
                    i += 1
                new_part += str(count)
            else:
                new_part += part[i]
                i += 1
        result.append(new_part.replace("x", "1"))
    return ' '.join(result)

def decomp(x):
    result = ''
    for c in x:
        if c.isdigit() and int(c) > 1:
            result += '0' * int(c)
        else:
            result += c
    return result


def enc(x):
    l = x.split()
    nl = []
    for c in l:
        if c[:2] == '11':
            marker = 'x'
            if c[-1] == '1': nl.append(marker + '2' + c[2:-1])
            elif c[-1] == '0': nl.append(marker + '1' + c[2:-1] + '0')
            else: nl.append(marker + c[1:])
        elif c[:2] != '11':
            marker = 'z'
            if c[-1] == '1': nl.append(marker + '2' + c[1:-1])
            elif c[-1] == '0': nl.append(marker + '1' + c[1:-1] + '0')
            else: nl.append(marker + c)
    nnl = []
    for c in nl:
        new_c = c
        new_c = new_c.replace('10', 'i')
        new_c = new_c.replace('111', 'm')
        new_c = new_c.replace('11', 'n')
        new_c = new_c.replace('22', 'j')
        new_c = new_c.replace('21', 'o')
        new_c = new_c.replace('23', 'f')
        nnl.append(new_c)
    nl = []
    for c in nnl:
        new_c = c
        new_c = new_c.replace('iii', 'k')
        new_c = new_c.replace('ixi', 'u')
        new_c = new_c.replace('iix', 'p')
        new_c = new_c.replace('ix', 'y')
        new_c = new_c.replace('xi', 'q')
        new_c = new_c.replace('zi', 's')
        new_c = new_c.replace('iz', 'w')
        nl.append(new_c)
    k = nl
    nl = []
    for c in k:
        nc = c.replace('201', 'd')
        nc = nc.replace('20', 'a')
        nl.append(nc)
    return ''.join(c for c in nl)
    
    
def dec(x):
    x = x.replace('a', '20').replace('d', '201')
    x = x.replace('k', 'iii').replace('p', 'iix').replace('y', 'ix').replace('q', 'xi').replace('s', 'zi').replace('w', 'iz').replace('u', 'ixi') 
    x = x.replace('m', '111').replace('i', '10').replace('n', '11').replace('j', '22').replace('o', '21').replace('f', '23')
    l = x.replace('x', 'hx').replace('z', 'hz').split('h')
    nl = []
    for c in l:
        if c[:2] == 'x2': nl.append('11' + c[2:] + '1')
        elif c[:2] == 'x1': nl.append( '1' + c[1:])
        elif c[:2] == 'z2': nl.append('1' + c[2:] + '1')
        elif c[:2] == 'z1': nl.append(c[1:])
    return ' '.join(c for c in nl)


__name__=''
s = string.ascii_lowercase + string.ascii_uppercase +string.digits + '+/'
if __name__ == 'a':
    print(s)
    x = turn_binary(s, 'To')
    print(x)
    x = comp(x)
    print(x)
    x = enc(x)
    print(x)
    y = dec(x)
    print(y)
    y = decomp(y)
    print(y)
    y = turn_binary(y, 'From')
    print(y)
    y = base64.b64decode(y).decode()
    print(y)
    print(view(y))

elif __name__ == 'b':
    usr = input("<= ")
    
    z = turn_binary(usr, 'To')
    print(z)
    z = comp(z)
    print(z)
    z = enc(z)
    print(z)
    m = dec(z)
    print(m)
    m = decomp(m)
    print(m)
    m = turn_binary(m, 'From')
    print(m)

elif __name__=='c':
    for c in s:
        z = enc(comp(turn_binary(c, 'to')))
        with open('all.txt', 'a') as f:
            f.write(c+':\n'+z+'\n'+dec(z)+'\n'+'\n')

else:
    print(s)
    print()
    z = enc(comp(turn_binary(s, 'to')))
    print(z)
    m = turn_binary(decomp(dec(z)), 'from')
    print()
    print(m)
    print()
    if m == s: print(True)
    else: print(False)

""" 








