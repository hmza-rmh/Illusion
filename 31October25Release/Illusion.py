import os
import re
import json
import base64
import string
import binascii
import time
from random import shuffle, randint as ri, choice as choi

# -------------------------
# Constants / small utilities
# -------------------------
class v:
    test_string = "A#bc ж ü ㅐ호 德苏 je m'appelle  ÿû!"
    const_list = ['111', '110', '101', '011', '100', '001', '010', '000', '+', '/']
    alt_list = [choi(string.ascii_uppercase) for _ in range(10)]
    errno1 = "There's nothing to compress or data type isn't string."
    const_chars = string.ascii_lowercase + '+/='

def chunk_s(s, CHUNK_SIZE=5*1024*1024):
    if len(s)>CHUNK_SIZE:
        return [s[i:i+CHUNK_SIZE] for i in range(0, len(s), CHUNK_SIZE)]
    else: return [s]

class asset:
    symbol = '¿'

def view(el):
    return "\n-----------------------------------------\n" + repr(el) + "\n-----------------------------------------\n"

# -------------------------
# Encoding helpers
# -------------------------
def enco(x):
    x = base64.b64encode(x).decode()
    return x.replace('=', '')

def deco(x):
    for _ in range(5):
        try:
            return base64.b64decode(x)
        except binascii.Error:
            x += '='

def turn_binary(element, direction):
    if not element:
        raise ValueError("A string or a binary are required.")
    if direction.lower() == 'to':
        return ' '.join(bin(ord(se))[2:] if se not in string.digits + '+/=' else se for se in element)
    elif direction.lower() == 'from':
        return ''.join(chr(int(se, 2)) if len(se) > 1 else se for se in element.split())
    else:
        raise ValueError("Please choose a valid direction for the string.(From/To)")

# -------------------------
# Text transformations
# -------------------------
def tpers(s, key):
    sen = ''.join(c for c in key)[-2:]
    return ''.join(
        c[0] + c[2].lower() if len(c) > 1 and c[1] != 'x' else
        c[0] + c[2] if len(c) > 1 else
        c if c in sen else
        c if c.isdigit() else c
        for c in s.split()
    )

def spert(s, key):
    parts, i, sen = [], 0, ''.join(c for c in key)[-2:]
    while i < len(s):
        if s[i] in sen:
            parts.append(s[i])
            i += 1
            continue
        elif s[i].isalpha() and i + 1 < len(s) and s[i + 1].isalpha():
            pair = s[i:i+2]
            if pair[1] in v.const_chars:
                parts.append(pair[0] + 'z' + pair[1].upper())
            else:
                parts.append(pair[0] + 'x' + pair[1])
            i += 2
        else:
            parts.append(s[i])
            i += 1
    return ' '.join(parts)

def unarrange(text):
    result = []
    C = 0
    while C + 9 <= len(text):
        block = text[C:C+9]
        groups = [block[j:j+3] for j in range(0, 9, 3)]
        rearranged = groups[::-1]
        result.extend(''.join(rearranged))
        C += 9
    result.extend(text[C:])
    return ''.join(result)

def comp(lst):
    encoded = [
        s[:3] + ('x' if s[3] == '0' else 'z') + s[4:] if len(s) >= 4 else s
        for s in lst
    ]
    return ' '.join(encoded)

def decomp(encr):
    return encr.replace('x', '0').replace('z', '1')

def zReplace(x, l1, l2):
    if not isinstance(x, str) or not x:
        raise TypeError("You seem to have not passed data.")
    if not l1 or not l2:
        raise KeyError("Cipher key is required.")
    x1 = x
    for s, y in zip(l1, l2):
        x = x.replace(s, y)
    if not x or x == x1:
        raise Exception("Something went wrong <@code:01>")
    return x

# -------------------------
# Key file parsing
# -------------------------
def getkey(file):
    if not file:
        raise ValueError("A path to a key is required.")
    if not os.path.exists(file):
        raise FileNotFoundError(f"The file <{file}> does not exist.")
    with open(file, 'r') as f:
        content, lst = f.read().split(), []
    if not content:
        raise ValueError("The given key file is empty.")
    for e in content:
        if not (e.startswith('<') and e.endswith('>')):
            raise ValueError(f"Invalid key format: {e}")
        lst.append(e[1:-1])
    return lst

# -------------------------
# Safe file generator
# -------------------------
def genfile(file):
    starter = ''
    if '/' in file:
        starter = file[:file.rfind('/')+1]
        basename = file[file.rfind('/')+1:]
    else:
        basename = file
    path = os.path.join(starter, basename)
    if not os.path.exists(path):
        msg = f'Created and added to file {path}'
        return path, msg
    name, ext = os.path.splitext(basename)
    existing_nums = []
    for f in os.listdir(starter or '.'):
        if f == basename:
            existing_nums.append(0)
        m = re.match(rf'^{re.escape(name)}\((\d+)\){re.escape(ext)}$', f)
        if m:
            existing_nums.append(int(m.group(1)))
    next_i = max(existing_nums, default=0) + 1
    if next_i >= 100:
        raise OSError('Failed to generate file, maximum copies (99)')
    new_name = f'{name}({next_i}){ext}'
    new_path = os.path.join(starter, new_name)
    return new_path, f'Created and added to file copy {new_path}'

# -------------------------
# Key generation / retrieval
# -------------------------
def switch(key: bytes, code=1, switch_file='switch.json') -> bytes:
    with open(switch_file, 'r') as f:
        switch = json.load(f)
    mapping = switch.get('char_swap', {})
    key_str = key.decode()
    if code == 1:
        swapped = ''.join(mapping.get(c, c) for c in key_str)
    else:
        inv = {v: k for k, v in mapping.items()}
        swapped = ''.join(inv.get(c, c) for c in key_str)
    return swapped.encode()

class genkey:
    @staticmethod
    def private(file='key.key'):
        if not file.endswith('.key'):
            file += '.key'
        if os.path.exists(file):
            file, msg = genfile(file)
        else:
            msg = f'Created and added to file {file}'
        symbol = asset.symbol
        st = ''
        chars = []
        n = 0
        while n < 10:
            ps = ''.join(choi(string.ascii_uppercase) for _ in range(100))
            np = ri(1, 100)
            po = np**3 / 3.141592653589793
            if ps[np-1] in chars:
                continue
            else:
                st += '<' + ps + '[' + str(po) + ']>' + (symbol if n != 9 else '')
                chars.append(ps[np-1])
                n += 1
        with open(file, 'w') as f:
            f.write(st)
        print(msg)
        return file

    @staticmethod
    def public(file='key.key'):
        if not os.path.exists(file):
            raise OSError(f'File »{file}« does not exist!')
        dirpart = os.path.dirname(file)
        basename = os.path.basename(file)
        pbasename = basename if basename.startswith('p') else 'p' + basename
        with open(file, 'r') as f:
            parts = f.read().split(asset.symbol)
        file_out, msg = genfile(os.path.join(dirpart, pbasename))
        n = 10
        st = ''
        for p in parts:
            n -= 1
            if not p:
                continue
            ps, po = p.split('[')
            po = float(po.replace(']>', ''))
            np = round((round(po * 3.141592653589793)) ** (1/3))
            r, k, d = ps[:np], ps[np], ps[np+1:]
            k = switch(k.encode()).decode()
            st += r + k + d + '[' + str(po) + ']>' + (asset.symbol if n != 0 else '')
        with open(file_out, 'w') as f:
            f.write(st)
        print(f'Key: {file_out} was created.')
        print(msg)
        return file_out

class getkey:
    @staticmethod
    def private(file='key.key'):
        key = b''
        if not os.path.exists(file):
            raise OSError(f'File »{file}« does not exist!')
        with open(file, 'r') as f:
            parts = f.read().split(asset.symbol)
        for p in parts:
            if not p:
                continue
            ps, po = p.split('[')
            po = float(po.replace(']>', ''))
            np = round((round(po * 3.141592653589793)) ** (1/3))
            key += ps[np].encode()
        print(f'Acquired the key: {key}')
        return key

    @staticmethod
    def public(file='pkey.key'):
        key = b''
        if not os.path.exists(file):
            raise OSError(f'File »{file}« does not exist!')
        with open(file, 'r') as f:
            parts = f.read().split(asset.symbol)
        n = 10
        for p in parts:
            n -= 1
            if not p:
                continue
            ps, po = p.split('[')
            po = float(po.replace(']>', ''))
            np = round((round(po * 3.141592653589793)) ** (1/3))
            c = ps[np]
            k = switch(c.encode(), code=2)
            key += k
        print(f'Acquired the key: {key}')
        return key

# -------------------------
# High-level encryption / decryption
# -------------------------
def enc(x, key):
    if not x:
        raise TypeError(v.errno1)
    if not key:
        raise KeyError('Cipher key is required.')
    x = x.encode() if isinstance(x, str) else x
    fst = enco(x)
    t = 5 * len(chunk_s(fst))-1
    bnr = turn_binary(fst, 'to')
    #time.sleep(t)
    snd = comp(bnr.split())
    trd = zReplace(snd, v.const_list, key)
    frt = tpers(trd, key)
    #time.sleep(t)
    return unarrange(frt)

def dec(x, key):
    if not isinstance(x, str) or not x:
        raise TypeError(v.errno1)
    if not key:
        raise KeyError('Cipher key is required.')
    t = 5 * len(chunk_s(x))-1
    fst = unarrange(x)
    #time.sleep(t)
    snd = spert(fst, key)
    trd = zReplace(snd, key[::-1], v.const_list[::-1])
    frt = decomp(trd)
    #time.sleep(t)
    nobnr = turn_binary(frt, 'from')
    return deco(nobnr)

# -------------------------
# Mathematical helpers
# -------------------------
def turn_position(intgr):
    return intgr ** 3 / 3.141592653589793

def get_position(flt):
    return round((round(flt * 3.141592653589793)) ** (1/3))

# -------------------------
# Main execution
# -------------------------
op = 'e'
if op == 'a':
    # generate 50 key pairs
    for _ in range(50):
        n = genkey.private('keyz/key.key')
        m = genkey.public(n)
        p = getkey.private(n)
        f = getkey.public(m)

    print('\nDone generating 50 key pairs.')
###
elif op == 'b':
    key = list(getkey.private('keyz/admin.key').decode())
    s = 'Hi, This is a secure string.'
    encrypted = enc(s, key)
    print(encrypted)
    decrypted = dec(encrypted, key)
    print(decrypted)
###
elif op == 'c':
    for i in range(1, 5):
        print(f'File: {i}')
        key = list(getkey.private('keyz/admin.key').decode())
        start = time.time()
        with open(f'FolderMI/{str(i)}.zip', 'rb') as f: content = f.read()
        print('Read'); end = time.time()
        print(f'Time: {end - start:.4f} seconds')
        start = time.time()
        x = enc(content, key)
        print('lowkey encrypted')
        with open(f're/result{str(i)}.enc', 'w') as f: f.write(x)
        print('Encrypted and wrote'); end = time.time()
        print(f'Time: {end - start:.4f} seconds')
        if not x:
            with open(f're/result{str(i)}.enc', 'r') as f: x = f.read()
        start = time.time()
        z = dec(x, key)
        with open(f'rer/myfile{str(i)}.zip', 'wb') as f: f.write(z)
        print('Decrypted and wrote'); end=time.time(); print(f'Time: {end - start:.4f} seconds'); print('Lovely!')
elif op == 'e':
    mode = int(input('Choose a mode:\n1-Static\n2-String only\n$< '))
    key = list(getkey.private('keyz/admin.key').decode())
    while True:
        s = input('<= ')
        if not s: continue
        if s.lower()=='chmod'.lower():
            mode = 2 if mode == 1 else 1
            print(f'Changed mode to: {"Static" if mode == 1 else "String only"}')
            continue
        if s.lower()=='kill'.lower(): print('return 0;'); break
        x = enc(s, key); print('e:', x)
        if mode == 1:
            y = dec(x, key); print('l:', len(x))
            print('d:', y.decode()); print('l:', len(y))
else: print('Lovely!')
##