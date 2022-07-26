'''Atbash Ciper'''
string1 = 'abcdefghijklmnopqrstuvwxyz'
string2 = 'zyxwvutsrqponmlkjihgfedcba'


def encrypt(string)
    t = ''
    s = string.split(" ")
    for i in s:
        for j in i.lower():
            indexing = string1.index(j)
            t += string2[indexing]
    return t

def decrypt(string)
    t = ''
    for i in string:
        indexing = string2.index(i)
        t += string1[indexing]
    return t



