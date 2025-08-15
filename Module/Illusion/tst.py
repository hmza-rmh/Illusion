#!/usr/bin/env python3
from script import *
from base64 import b64encode as be
from base64 import b64decode as de
with open('file.zip', 'rb') as f:
    cont = f.read()
x = enc(comp(turn_binary(be(cont).decode(), 'to')), getkey('jsOKIUvkruoaPSwfimJyFdpGLnqA.txt'))
with open('file.txt', 'w') as f:
    f.write(x)
    print('stored.')
"""
y = de(turn_binary(decomp(dec(x)), 'from'))
with open('file2.zip', 'wb') as f:
    f.write(y)
    print('stored.')
"""