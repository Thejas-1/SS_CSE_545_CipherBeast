
def GenerateKey(Message,origKey):
    if len(Message)==len(origKey):
        return ''.join(origKey)
    key=''
    ind=0
    for i in range(len(Message)):
        if Message[i]!=' ':
            key+=origKey[ind%len(origKey)]
            ind+=1
    return key

def GenerateCipher(Message,key):
    cipher=[]
    Message=''.join(list(Message.split(' ')))
    for i in range(len(key)):
        val=(ord(Message[i])+ord(key[i]))%26
        val+=ord('A')
        cipher.append(chr(val))
    return ''.join(cipher)

def decodeOriginalText(cipherText,key):
    origText=[]
    for i in range(len(key)):
        val=(ord(cipherText[i])-ord(key[i])+26)%26
        val+=ord('A')
        origText.append(chr(val))
    return "".join(origText)

if __name__=='__main__':
    PlainText = "ARIZONASTATEUNIVERSITY"
    cipherText = "EUCDRHEVNEWYYQCZHLWLNC"
    alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    keysCount = 0
    with open('keys.txt', 'w') as f:
        for i in range(0,26):
            keysCount = keysCount+1
            key=GenerateKey(PlainText,alphabets[i])
            keyCipher = GenerateCipher(PlainText,key)
            if keyCipher == cipherText:
                print("key: "+alphabets[i]+", true")
            f.write(alphabets[i]+'\n')
            #else:
            #    print("key: "+alphabets[i]+", false")
        for i in range(0,26):
            for j in range(0,26):
                keysCount = keysCount+1
                key=GenerateKey(PlainText,alphabets[i]+alphabets[j])
                keyCipher = GenerateCipher(PlainText,key)
                if keyCipher == cipherText:
                    print("key: "+alphabets[i]+alphabets[j]+", true")
                f.write(alphabets[i]+alphabets[j]+'\n')
                #else:
                #    print("key: "+alphabets[i]+alphabets[j]+", false")
        for i in range(0,26):
            for j in range(0,26):
                for k in range(0,26):
                    keysCount = keysCount+1
                    key=GenerateKey(PlainText,alphabets[i]+alphabets[j]+alphabets[k])
                    keyCipher = GenerateCipher(PlainText,key)
                    if keyCipher == cipherText:
                        print("key: "+alphabets[i]+alphabets[j]+alphabets[k]+", true")
                    f.write(alphabets[i]+alphabets[j]+alphabets[k]+'\n')
                    #else:
                    #    print("key: "+alphabets[i]+alphabets[j]+alphabets[k]+", false")
        print("keysCount: "+str(keysCount))
        f.write("keysCount: "+str(keysCount))
