def caesar_cipher_attack(encrypted_text):
    english_character_frequencies = {'a':  0.080,  'b':  0.015,  'c': 0.030 ,  'd':  0.040,  'e':  0.130,  'f':  0.020,  'g':  0.015,  'h': 0.060 ,  'i': 0.065 ,  'j': 0.005 ,  'k': 0.005 ,  'l': 0.035 ,  'm': 0.030 ,  'n': 0.070 ,  'o': 0.080 ,  'p': 0.020 ,  'q': 0.002 ,  'r': 0.065 ,  's': 0.060 ,  't': 0.090 ,  'u': 0.030 ,  'v': 0.010 ,  'w': 0.015 ,  'x': 0.005 ,  'y': 0.020 ,  'z':  0.002  }
    cipher_freq = {}
    for character in encrypted_text:
        if cipher_freq.get(character)==None:
            cipher_freq[character] = 1
        else:
            cipher_freq[character] = cipher_freq[character]+1
    for key in cipher_freq:
        cipher_freq[key] = cipher_freq[key]/len(encrypted_text)
    correlation = {}
    for i in range(26):
        corr = 0;
        for key in cipher_freq:
            corr+=cipher_freq[key]*english_character_frequencies[chr(ord('a')+(ord(key)-ord('a')-i+26)%26)]
        correlation[i] = corr
    for key in sorted(correlation, key=correlation.get, reverse=True):
        plausible_answer = ""
        for char in encrypted_text:
            plausible_answer = plausible_answer+caesar_decipher(char,key)
        print(plausible_answer)
        
def caesar_decipher(character,key):
    return chr(ord('a')+(ord(character)-ord('a')-key+26)%26)
    
    
encrypted_text = input("Enter the encrypted text: ")
caesar_cipher_attack(encrypted_text)
