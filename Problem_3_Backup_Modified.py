
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

def GenerateCipher(Message,key1,key2):
    cipher=[]
    Message=''.join(list(Message.split(' ')))
    for i in range(len(key1)):
        val=(ord(Message[i])+ord(key1[i])-ord(key2[i]))%26+1
        val+=ord('A')
        cipher.append(chr(val))
    return ''.join(cipher)

def decodeOriginalText(cipherText,key1,key2):
    origText=[]
    for i in range(len(key1)):
        val=(ord(cipherText[i])-ord(key1[i])+ord(key2[i])+26)%26-1
        val+=ord('A')
        origText.append(chr(val))
    return "".join(origText)

if __name__=='__main__':
    Message = "THE BOY HAS THE BALL"
    origKey = ['Y', 'X', 'Z']
    secondKey = ['N','P','Q']
    key1=GenerateKey(Message,origKey)
    key2=GenerateKey(Message, secondKey)
    print('MESSSAGE TO BE CIPHERED: ',Message)
    print('KEYS: ',key1,key2)
    cipherText=GenerateCipher(Message,key1,key2)
    print('CIPHER TEXT: ',cipherText)
    origText=decodeOriginalText(cipherText,key1,key2)
    print('ORIGINAL TEXT: ',origText)
