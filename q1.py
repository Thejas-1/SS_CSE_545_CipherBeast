def caesar_cipher(plainText,key):
    if(key<0 or key>25):
        return "Key should belong to range of 0 to 25"
    ans = ""
    for char in plainText:
        if(ord(char)<65 or ord(char)>90):
            return "All letters in the plain text should be capital english alphabets."
        ans = ans+chr((ord(char)+int(key)-ord('A'))%26+ord('A'))
    return ans
    
plainText = input("Enter the character to be encrypted (Should be a capital letter): ")
key = int(input(("Enter the key value (It should be between 0 and 25): ")))
print(caesar_cipher(plainText,key))
