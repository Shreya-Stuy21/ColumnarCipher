# ColumnarCipher
Decryption software on how to break the double transposition cipher. 

I developed a tool to run a dictionary attack on the Columnar Cipher. The Columnar Cipher can easily be encrypted or decrypted using a given key. However, what happens when you don't know what the key is? You have to guess the key length, and try all permutations of the key to decrpyt the ciphertext. This tool automates that process for you.

To run this code you have to compile (javac Bruteforce.java), and then type java Bruteforce. The shell will prompt you to answer a few questions (encrypt/decypt?). It does so using Scanner (you can also substitute Buffered Reader). Bruteforce.java provides many instructions to the output stream (your command prompt) to guide you on how to use Bruteforce and what arguments you should enter. For more on how to use Bruteforce, scroll below.

Bruteforce.java has many uses, but it's main functionality is to break a cipher by finding all the sequences of key permutations. It will then run the result of each permutations' plaintext through a dictionary, and record the number of words it found in a separate plaintext file.

To encrypt, provide the plaintext you want to encrypt, as well as the key you want to encrypt it with. For example, if my keyword is "apple", I would enter any plaintext, and then I would enter "14532" based on the order a, p, p, l and e appear in the alphabet. (You can also enter "15432", since there are two Ps. I prefer to run the first P first). *IMPORTANT: Do NOT start with 0 as an index, since the program already accounts for that by subtracting one from every imdex*

To decrypt, simply provide the cyphertext, and a number n, to try all permutations. This automatically generates a file, ColumCipherOutput.txt, that has stored each permutation's plaintext, a few lists of the words it found in the plaintext, along with the number of words. It should be noted that for each correct key, there will likely be more than one word list since there are words within words that the dictionary will find.

Encryption is optional but decryption is necessary. That means no matter what, Bruteforce.java will decrypt some text. You can either provide your own ciphertext or use the program's encrypt function to generate cyphertext for the program to decrypt.

Any questions? Found bugs? Want to give tips? Email me at shreyash618@gmail.com.

Credits to my mom for helping me format this.
#copyright@2021 Shreya Shukla
