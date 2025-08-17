# Illusion
##### _Binary-based-encryption_

Illusion is a binary based encryption/decryption algorithm, that was made in 23 hours (as for the first release).
Make sure to read this file to know how it functions.


``````py
from script import * #import all functions

""" First Generate your Key """
""" list the pre-assigned variable const_string form the class v, and use True if you want to generate a file for the key (the function returns key path """
key_path = genkey(list(v.const_string), "key.key")

""" Get your key info from file path """
key = getkey(key_path)

""" Get the binary of the base64 string or whatever string you want (There are limitations for character choice), encoding it using base64 is highly recommended """
my_binary = turn_binary("Some_Encoded_String", "to")

""" Compress the the binary """
comp_bin = comp(my_binary)

""" Encrypt your data """
""" using your key and string of compressed binary """

encrypted = enc(comp_bin, key)

""" Now reverse """

""" Decrypt data """
decrypted = dec(encrypted, key)

""" Decompress decrypted data """
decomp = decomp(decrypted)

""" Get back your string """
stringed_back = turn_binary(decomp, "from")

""" That's pretty much everything you need to know """
``````
##### Stay tuned for future updates, contact info are in contactme.md
#### – Dev
