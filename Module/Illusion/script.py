import json, base64, os
from random import shuffle, randint as ri


class v: test_string, const_list, const_string = "A#bc ж ü ㅐ호 德苏 je m'appelle  !", ['10', '111', '11', '22', '21', '23', 'iii', 'ixi', 'iix', 'ix', 'xi', 'zi', 'iz', '201', '20', 'xoi', 'z25', '12', 'ii', 'xn', 'xo', '13', '14', 'Gz', 'Gi', '2x', '3x', '3z'], "imnjoBkuypqwdaDvrGKOUPIALJFS"; errno1 = "There's nothing to compress or data type isn't string." 

def view(el):
    return "\n-----------------------------------------\n" + repr(el) + "\n-----------------------------------------\n"

def reduce(x):
    if not isinstance(x, str) or not x: raise TypeError(v.errno1)
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
    return nl

def re_reduce(x):
    if not isinstance(x, str) or not x: raise TypeError(v.errno1)
    l = x.replace('x', 'hx').replace('z', 'hz').split('h')
    nl = []
    for c in l:
        if c[:2] == 'x2': nl.append('11' + c[2:] + '1')
        elif c[:2] == 'x1': nl.append( '1' + c[1:])
        elif c[:2] == 'z2': nl.append('1' + c[2:] + '1')
        elif c[:2] == 'z1': nl.append(c[1:])
    return nl

def zReplace(x, l1, l2):
    if not isinstance(x, str) or not x: raise TypeError("You seem to have not passed data.")
    if not l1 or not l2: raise KeyError("Cipher key is required.")
    x1 = x
    for s, y in zip(l1, l2): x = x.replace(s, y)
    if not x or x == x1: raise Exception("Something went wrong <@code:01>")
    return x
        

def getkey(file):
    if not file: raise ValueError("A path to a key is required to complete this operation.")
    if not os.path.exists(file): raise FileNotFoundError(f"The file <{file}> does not exist.")
    try:
        with open(file, 'rb') as f:
            content, lst = f.read().decode().split(), []
    except UnicodeDecodeError as e: print(e); return []
    if not content: raise ValueError("The given key file is empty.")
    for e in content:
        if not (e.startswith("<") and e.endswith(">")): raise ValueError(f"Invalid key format: {e} (expected <{e}>)")
        lst.append(e[1:-1])
    return lst

def genkey(el, file=""):
    if not el or not isinstance(el, list): raise ValueError("A list is required.")
    shuffle(el)
    if file: fn, res, ext = file, file[:file.rfind('.')], file[file.rfind('.'):]
    else: res, ext = ''.join(c for c in el), '.txt'; fn = f'{res}' + ext
    if os.path.exists(fn):
        for i in range(1, 100):
            fn = f'{res}' + str(i) + ext
            if not os.path.exists(fn): break
            if i == 99: raise ValueError("Couldn't apply a copy for <{format}> where it has reached the maximum number of copies, please consider using another file name.")
    try:
        with open(fn, 'w') as f:
            for c in el: f.write(f"{ri(0, 99)*' '}<{c}>\n")
    except OSError as e: print('File write error:', e); return el
    return fn

def turn_binary(element, direction):
    if not element: raise ValueError("A string or a binary are required.")
    if direction.lower() == 'to': return ' '.join(bin(ord(se))[2:] for se in element)
    elif direction.lower() == 'from': return ''.join(chr(int(se, 2)) for se in element.split())
    else: raise ValueError("Please choose a valid direction for the string.(From/To)")

def comp(x):
    if not isinstance(x, str) or not x: raise TypeError(v.errno1)
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
    if not isinstance(x, str) or not x: raise TypeError(v.errno1)
    return ''.join('0' * int(c) if c.isdigit() and int(c) > 1 else c for c in x)


def enc(x, key):
    if not isinstance(x, str) or not x: raise TypeError(v.errno1)
    if not key: raise KeyError("Cipher key is required.")
    nl = reduce(x); res = zReplace(''.join(c for c in nl), v.const_list, key)
    return res

def dec(x, key):
    if not isinstance(x, str) or not x: raise TypeError(v.errno1)
    if not key: raise KeyError("Cipher key is required.")
    b = zReplace(x, key[::-1], v.const_list[::-1]); nl = re_reduce(b)
    return ' '.join(c for c in nl)


if __name__ == '__main__':
    
    key = getkey('key.key')
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
