# Cracking ADFGX
This project provides python code for cracking an ADFGX cipher with a key length of 8, 9, or 10.

## Code Explanation
* adfgx.py:
    
    My original take on cracking the cipher. It only uses half of the ciphertext, so it's best for very long messages. You must have an idea of the key length first, and this code is setup for a key length of 8, 9, or 10. Before running the code, make sure new lines and spaces are removed from the ciphertext, the letters are capitalized, and that `str` is set to this single string. Next, change `numCols` to the desired key length, and then uncomment the initialization of `candFreq` that corresponds to the number of columns (first is 8, second is 9, and third is 10).
    
    Run the code in the folder containing the file using: `python adfgx.py`
    
    The number of English-like permutation orders and the frequency of each column number in each position will be printed to the console.
* v2_adfgx.py:

    My second take on cracking the cipher. It uses all of the ciphertext, so it may take a long time to run. Like the original adfgx.py, you must have an idea of the key length first, and this code is setup for a key length of 8, 9, or 10. Before running the code, make sure new lines and spaces are removed from the ciphertext, the letters are capitalized, and that `str` is set to this single string. Next, change `numCols` to the desired key length, and then uncomment the initialization of `candFreq` that corresponds to the number of column (first is 8, second is 9, and third is 10).
    
    Run the code in the folder containing the file using: `python v2_adfgx.py`
    
    The number of English-like permutation orders and the frequency of each column number in each position will be printed to the console.
* bi2mono.py:

    An easy way to substitute single letters for pairs of letters found in an ADFGX grid. The pairs of letters must be separated only by spaces and set in a single string to the variable `ct`.
    
    The substituted version of the pairs of letters will be printed out in a single string to the console that can then be analyzed like a monoalphabetic cipher.

## Steps for Cracking the Cipher
You can use either of the ADFGX python files to find the possible transposition orderings, but it your computer can stand it, the `v2_adfgx.py` file is better.

1. Use this [tool](http://rumkin.com/tools/cipher/manipulate.php) to change the ciphertext to uppercase and remove all spaces and newlines. The tool will tell you how many uppercase letters there are, so find the factors of that number to select a key length.

2. Set `str` equal to the altered ciphertext from 1.

3. Set `numCols` equal to the key length that you selected from the factors of the total number of letters.

4. If `numCols` is not equal to 9 (the default in this code), then also make sure to comment out the current initialization of `candFreq` and uncomment your desired initialization (first is 8, second is 9, and third is 10).

5. Run the program using the following command: `python v2_adfgx.py`

    The output to the console should look something like this:  
    `[[0, 0, 0, 0, 0, 1, 0, 0, 0], `   
    ` [1, 0, 0, 0, 0, 0, 0, 0, 0], `  
    ` [0, 0, 0, 0, 0, 0, 0, 1, 0], `   
    ` [0, 0, 0, 0, 0, 0, 1, 0, 0], `  
    ` [0, 0, 0, 0, 0, 0, 0, 0, 1], `   
    ` [0, 1, 0, 0, 0, 0, 0, 0, 0], `  
    ` [0, 0, 1, 0, 0, 0, 0, 0, 0], `  
    ` [0, 0, 0, 0, 1, 0, 0, 0, 0], `  
    ` [0, 0, 0, 1, 0, 0, 0, 0, 0]]`
    
    This grid shows the count of each column number (1-9) in each position (1-9). The first row in this grid represents the first position of the transposition matrix, and each value in that row is the number of times each transposition column was in that position for all of the top candidate orderings (top meaning their index of coincidence was above 0.06, which is nearest to English). 
    
    This sample grid tells us that the ordering of the columns for columnar transposition is 6-1-8-7-9-2-3-5-4, or FAHGIBCED.
    
6. Take the original ciphertext to this [website](http://web.archive.org/web/20131031100144/http://home.comcast.net/~acabion/mysz4.html) and paste it into the text box. Input the key length that you used in the python program and click "Initialize". Next, reorder the columns according to the output from the program; since this website uses letters to label the columns, use FAHGIBCED for the example.

7. Click "Decrypt using current columns" at the bottom of the page and copy the text. Paste this text (with the bottom "key" information removed) back into the [text manipulator](http://rumkin.com/tools/cipher/manipulate.php). Change the text to uppercase, make groups of 2, and then remove newlines.

8. Place this new text into the `ct` variable of `bi2mono.py`. Run the program using `python bi2mono.py` in the folder in which the file is saved. (Note: You can easily do this online using [this online compiler](https://www.tutorialspoint.com/execute_python_online.php). Just copy the code from `bi2mono.py` into the left side of the page and press "Execute".) The output will be a monoalphabetic version of the paired letters using the following key:

    `_  A  D  F  G  X `  
    `A  A  B  C  D  E `  
    `D  F  G  H  I  K `  
    `F  L  M  N  O  P `  
    `G  Q  R  S  T  U `  
    `X  V  W  X  Y  Z `  
    
    The letters DA, for example, will be mapped to the letter B, the letters GF to O, and so on. 
    
9. Take the output from 8 and analyze the unigram, bigram, and trigram frequencies [here](http://practicalcryptography.com/cryptanalysis/text-characterisation/monogram-bigram-and-trigram-frequency-counts/) and start cracking the monoalphabetic cipher [here](http://www.mcld.co.uk/decipher/). Soon, you'll have cracked ADFGX!

