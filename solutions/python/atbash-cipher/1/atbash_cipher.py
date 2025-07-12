import re
def encode(plain_text):
    cipher=str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ','zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba')
    encoded=plain_text.translate(cipher)
    encoded=re.sub('[^a-zA-Z0-9]','',encoded)
    divided_encoded=''
    for idx,char in enumerate(encoded):
        divided_encoded+=char
        if not (idx+1)%5 and idx!=len(encoded)-1:
            divided_encoded+=' '
    return divided_encoded
def decode(ciphered_text):
    decipher=str.maketrans('abcdefghijklmnopqrstuvwxyz','zyxwvutsrqponmlkjihgfedcba')
    decoded=ciphered_text.translate(decipher)
    return decoded.replace(' ','')
