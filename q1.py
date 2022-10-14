def caesar_cipher(plainText,key):
    if(key<0 or key>25):
        return "Key should belong to range of 0 to 25"
    ans = ""
    for char in plainText:
        if(ord(char)<65 or ord(char)>90):
            return "All letters in the plain text should be capital english alphabets."
        ans = ans+chr((ord(char)+int(key)-ord('A'))%26+ord('A'))
    return ans
    
plainText = "HELLO"
key = 3
print(caesar_cipher(plainText,key))
