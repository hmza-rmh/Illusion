import json, base64, os
from random import shuffle


class v: test_string, const_list, const_string = "A#bc ж ü ㅐ호 德苏 je m'appelle  !", ['10', '111', '11', '22', '21', '23', 'iii', 'ixi', 'iix', 'ix', 'xi', 'zi', 'iz', '201', '20', 'xoi', 'z25', '12', 'ii', 'xn', 'xo', '13', '14', 'Gz', 'Gi', '2x', '3x', '3z'], "imnjofkuypqwdasvrGKOUPIALJFS"

def view(el):
    return "\n-----------------------------------------\n" + repr(el) + "\n-----------------------------------------\n"

def zReplace(x, l1, l2):
    for s, y in zip(l1, l2): x = x.replace(s, y)
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
    return fFormat

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


def enc(x, key):
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
    res = zReplace(''.join(c for c in nl), v.const_list, key)
    return res
    
    
def dec(x, key):
    b = zReplace(x, key, v.const_list)
    l = b.replace('x', 'hx').replace('z', 'hz').split('h')
    nl = []
    for c in l:
        if c[:2] == 'x2': nl.append('11' + c[2:] + '1')
        elif c[:2] == 'x1': nl.append( '1' + c[1:])
        elif c[:2] == 'z2': nl.append('1' + c[2:] + '1')
        elif c[:2] == 'z1': nl.append(c[1:])
    return ' '.join(c for c in nl)


if __name__ == '__main__':
    
    key = getkey('jsOKIUvkruoaPSwfimJyFdpGLnqA.txt')
    print(key)
    s = v.test_string
    s = base64.b64encode(s.encode()).decode()
    print(s)
    x = turn_binary(s, 'To')
    print(x)
    x = comp(x)
    print(x)
    x = enc(x, key)
    print(x)
    y = dec(x, key)
    print(y)
    y = decomp(y)
    print(y)
    y = turn_binary(y, 'From')
    print(y)
    y = base64.b64decode(y).decode()
    print(view(y))
    print()
