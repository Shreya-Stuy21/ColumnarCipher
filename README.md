# ColumnarCipher
Decryption software on how to break the double transposition cipher. 

I developed a tool to run a dictionary attack on the Columnar Cipher. The Columnar Cipher can easily be encrypted or decrypted using a given key. However, what happens when you don't know what the key is? You have to guess the key length, and try all permutations of the key to decrpyt the ciphertext.

This was super inefficient, so I maintained a max length of 9 characters in a word.

To run this code you have to run javac Col_Trans.java, and then run java with an integer n (a proposed key length to break the cipher). 
