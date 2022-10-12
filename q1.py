def caesar_cipher():
    plainText = input("Enter the character to be encrypted (Should be a capital letter): ")
    key = input("Enter the key value (It should be between 0 and 25): ")
    print((ord(plainText)+int(key)))
    print(chr((ord(plainText)+int(key)-ord('A'))%26+ord('A')))
    
caesar_cipher()
