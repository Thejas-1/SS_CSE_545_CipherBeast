

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

def GenerateCipher(Message,key,asciiStart):
    cipher=[]
    Message=''.join(list(Message.split(' ')))
    for i in range(len(key)):
        val = (ord(Message[i])-ord('A')+ord(key[i])-ord('A'))%26
        val+=asciiStart
        cipher.append(chr(val))
    return ''.join(cipher)

def decodeOriginalText(cipherText,key,asciiStart):
    origText=[]
    for i in range(len(key)):
        val=(ord(cipherText[i])-asciiStart-ord(key[i])-ord('A'))%26
        val+=ord('A')
        origText.append(chr(val))
    return "".join(origText)

def validateKey(key):
    for c in key:
        if 'A'<=c<='Z':
            continue
        else:
            return False
    return True

if __name__=='__main__':
    Message = input('Enter your plain text: ')
    origKey = input('Enter your key:')
    if not validateKey(origKey) or len(origKey)>3:
        print('Key should contain uppercase letters between A to Z and should be 3 characters long.')
    else:
        asciiStart =101
        key=GenerateKey(Message,origKey)
        print('MESSSAGE TO BE CIPHERED: ',Message)
        print('KEY: ',key)
        print('ASCIISTART: ',asciiStart)
        cipherText=GenerateCipher(Message,key,asciiStart)
        print('CIPHER TEXT: ',cipherText)
        origText=decodeOriginalText(cipherText,key,asciiStart)
        print('ORIGINAL TEXT: ',origText)