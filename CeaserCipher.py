def main():
    function =raw_input("If you would like to encrypt something enter 'e' else if you would like to decrypt something enter 'd'\n")
    text = raw_input("would you like to like to open from a textfile or paste the text in 'f' for file, all else will paste")
    if function == "e":
        encrypt(text)
    elif function == "d":
        decrypt(text)



def increaseVal(val, inc):
    newVal = ord(val)
    if(newVal<= 122) and (newVal>=97):
        newVal = newVal - 97 + inc # decrease by 97 the value of a +n for the rotation amount
        newVal = newVal%26 +97 # interger division incase the letter was z it now will be an
    if((newVal<=90) and (newVal >= 65)):
        newVal = newVal - 65 + inc  # decrease by 97 the value of a +n for the rotation amount
        newVal = newVal % 26 + 65  # interger division incase the letter was z it now will be an
    return chr(newVal)

def getEInput(text):
    if text =="f":
        plain = open("PlainText/Ceaser.txt").read()
    else:
        plain = raw_input("What would you like to ceaser shift\n")
    rotation = eval(raw_input("What number would you like to rotate it\n"))
    return plain, rotation

def getDInput(text):
    if text == "f":
        cipherText = open("CipherText/Ceaser.txt").read()
    else:
        cipherText = raw_input("What is the ciphered Text\n")
    rotation = eval(raw_input("What is the rotation value (if unknown write 0"))
    return cipherText, rotation

def encrypt(text):
    plainText, rotationVal = getEInput(text)
    message = ""
    for val in plainText:
        message +=  increaseVal(val, rotationVal)
    print message

def decrypt(text):
    cipherText, rotation = getDInput(text)
    message = ""
    if (rotation != 0):
        for val in cipherText:
            message += increaseVal(val, (26-rotation))
        print (message)
    else:
        for i in range (1,26):
            message = "Rotation " + str(i)+"\n"
            for val in cipherText:
                message += increaseVal(val, 26-i)
            print (message)
main()