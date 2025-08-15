from script import *
import base64

key = getkey('key.txt')
strn = base64.b64encode('Hi, I am Taio!'.encode()).decode()
print(enc(comp(turn_binary(strn, 'to')), key))