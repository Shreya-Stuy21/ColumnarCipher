import itertools; ## import itertools to get permutations (this way you don't have to generate permutations yourself)
from pycipher import ColTrans; ## visit https://pycipher.readthedocs.io/en/master/#columnar-transposition-cipher
## m must be an integer
def different_perms (m): 
    key_length = {}
    for x in range(m):
        key_length[i] = i
    perms = itertools.permutations (key_length)
    return perms
## 
def dictionary (file):
    f = open("Ten_Thousand_Most_Common", "r")
    return f.read().split()
def columnar_brute_force (key_length):
    perms = different_perms(7) ##input can be any number, we are trying 7 ## this would be key_length
    col_pos = {}
    for perm in perms:
        col_pos = col_pos + perm
        col_pos = col_pos + ColTrans(perm).decipher (cyphertext)
    return col_pos.split()


def dictionary_atack (text, file):
    f = open("plaintext_words.txt", "w")
    sortedWords = {}
    words = dictionary ("Ten_Thousand_Most_Common")
    for word in words:
        if word in sortedWords:
            sortedWords = sortedWords + word
    for i in sortedWords:
        f.write(i + "/n")
    f.close


    
    