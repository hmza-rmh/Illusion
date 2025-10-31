# Illusion algorithm

## Overview
Another encryption algorithm boiz! :D
**DES** in **ECP** mode ( no HMAC, no IVs ),
With some **position swapping** that makes it unique in its own way.

## Features
- Unique **10 byte key** storing and usage.
- Unique encryption with **expansion ratio** up to 4×
- It's been like 3 months since i made it so i don't actually remember more details 😅

## Used modules
import os
import re
import json
import base64
import string
import binascii
import time
from random import shuffle, randint as ri, choice as choi

## Examples
```python
from Illusion import *

s = "I don't know just a string"

f = genkey.private('mykey.key')
#f = 'mykey.key'
k = list(getkey.private(f).decode())

encrypted = enc(s, k)

print(encrypted)
print(dec(encrypted, k).decode()) # Back to normal state
```

## Notes / Tips
**Never** use it on files **larger than** 1MB, it's not built for that.

If your sentence **ends with** ! - ? - or any punctuation **add a b'space! '**. nvm it appears that I've fixed that bug :)

When i said unique in this markdown i didn't mean that it's necessarily Unique, encryption has been there since forever so someone mightve had this idea but i just am not into cryptography world that much.

The naming was random please don't sue me :)