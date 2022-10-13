def caesar_cipher():
    flag1=True

    while flag1:
        plainText = input("Enter the character to be encrypted (Should be a capital letter): ")

        if len(plainText)==1:
            if (65<=ord(plainText)<=90):
                flag1 = False
            else:
                print('Character Should be a capital letter')
        else:
            print('Character Should be a capital letter')

    flag1=True

    while flag1:
        key = input("Enter the key value (It should be between 0 and 25): ")
        if '0'<=key<='25':
            flag1=False
        else:
            print("Key should be between 0 and 25")
    print('Encryption Code: ',(ord(plainText)+int(key)))
    print('Encrypted Text: ',chr((ord(plainText)+int(key)-ord('A'))%26+ord('A')))
    
caesar_cipher()
