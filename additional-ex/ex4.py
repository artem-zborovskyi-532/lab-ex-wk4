# Exercise 4: extension of week 3 exercise 5
    # In cryptography, a Caesar cipher, also known as the shift cipher, is one of the
    # simplest and most widely known encryption techniques. It is a type of substitution
    # cipher in which each letter in the plain text is replaced by a letter some fixed
    # number of positions down the alphabet.
    # For example, with a shift of 3, A would be replaced by D, B would become E, and
    # so on. The method is named after Julius Caesar, who used it to communicate with
    # his generals.
        # Mathematically, a Caesar cipher can be
        # expressed by the following equation:
        # c = (p + a) mod 26
        # Here, ‘mod 26’ means that you use clock
        # arithmetic for values greater than 26, i.e.,
        # 0=26 mod 26, 1=27 mod 26, 2=28 mod 26, …,
        # 0=52 mod 26, 1=53 mod 26, …, 10=62 mod
        # 26, and so on.
            # 1. Write a function caesar_encrypt that encrypts a plain text into a cypher
            # text using the Caesar Cipher algorithm. What parameters are needed?
            # Should the function return something? For simplicity, assume that only
            # alphabet letters are encrypted, other symbols remain the same.

            # 2. Write a function caesar_decrypt that decrypts a cipher text into a plain
            # text using the Caesar Cipher algorithm. What parameters are needed?

            # 3. Given the cipher text below, and knowing it has been encrypted using a
            # Caesar Cipher algorithm, could you decrypt it?
                # "bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc
                # bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc
                # bmtt bpmu bw lw.”

# Parts 1 and 2 are solved -> artem-zborovskyi-532/lab-ex-wk2/ex5.py

def is_plain(s: str) -> bool:
    return all(c.isalpha() or c.isspace() for c in s)

def letter_pos(letter: str) -> int:
    letter = letter.lower()
    return ord(letter) - ord('a') + 1

def letter_from_pos(pos: int, upper: bool) -> str:
    return chr(ord('a') + pos - 1).upper() if upper == True else chr(ord('a') + pos - 1);

def caesar_decrypt(text:str, shift: int) -> str:
    res = ""
    for char in text:
        if char == " ":
            res += char
            continue
        if is_plain(char) == False:
            res += char
            continue
        c = (letter_pos(char) - shift) % 26
        res += letter_from_pos(c, char.isupper())

    print(f"{shift} ) {res}")

encryptedText = ("bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc " + 
                "bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc " + 
                "bmtt bpmu bw lw.")

for i in range(27):
    caesar_decrypt(encryptedText, i)

# It takes shift = 8 (or 9 if we don't count shift = 0 as a shift) to decrypt provided text:
# the good news about computers is that they do what you tell them to do. 
# the bad news is that they do what you tell them to do.