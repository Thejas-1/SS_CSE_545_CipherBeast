
def GenerateKey(Message,origKey):
    if len(Message)==len(origKey):
        return ''.join(origKey)
    key=''
    values=Message.split(' ')
    cipher=''
    ind=0
    alphabets={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S'
               ,19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    for i in range(len(Message)):
        if Message[i]!=' ':
            key+=origKey[ind%len(origKey)]
            ind+=1
    return key

def GenerateCipher(Message,key):
    cipher=[]
    Message=''.join(list(Message.split(' ')))
    for i in range(len(key)):
        val=(ord(Message[i])+ord(key[i]))%26+1
        val+=ord('A')
        cipher.append(chr(val))
    return ''.join(cipher)

def decodeOriginalText(cipherText,key):
    origText=[]
    for i in range(len(key)):
        val=(ord(cipherText[i])-ord(key[i])+26)%26-1
        val+=ord('A')
        origText.append(chr(val))
    return "".join(origText)

if __name__=='__main__':
    Message = "THE BOY HAS THE BALL"
    origKey = ['Y', 'X', 'Z']
    key=GenerateKey(Message,origKey)
    print('MESSSAGE TO BE CIPHERED: ',Message)
    print('KEY: ',key)
    cipherText=GenerateCipher(Message,key)
    print('CIPHER TEXT: ',cipherText)
    origText=decodeOriginalText(cipherText,key)
    print('ORIGINAL TEXT: ',origText)
