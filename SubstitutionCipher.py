import FrequencyAnalyser


def subCipher(file):

    freq = FrequencyAnalyser.analyser(file)
    letterOcc = FrequencyAnalyser.frequencyOrder(freq)
    commonLetters = leterFreq()
    file = forceSwitch(file,letterOcc,commonLetters)
    #file = commonSwitch(file,letterOcc,commonLetters)
    askSwitch(file)
    print(file)

def commonSwitch(file, letterOcc, commonLetters):

    for i in range (5):
        print("the most common letters are")
        print(commonLetters)
        mostPop = letterOcc[i]
        message = "the " + str((i+1)) + " most common letter is " + str(mostPop) + " which letter would you like to replace it with\n"
        inp= raw_input(message)
        file = replaceLetters(file,mostPop, inp)
    return file

def askSwitch(file):
    carry = True
    print("the message currently reads")
    print(file)
    message = ""
    while carry:
        change = raw_input("What letter would you like to change (case Sensitive)\n")
        to = raw_input("What would you like to change it to?\n")
        file = replaceLetters(file, change, to)
        print("the message currently reads")
        print(file)
        message += change + " has been changed to " + to + "\n"
        carryon = raw_input("Would you like to change another? y/n \n")
        if carryon == "n":
            carry= False



def forceSwitch(file, letterOcc, commonLetters):
    temptext = list(file)
    for i in range(len(commonLetters)):
        letter = letterOcc[i]
        switch = commonLetters[i]
        for char in range(len(file)):
            if file[char] == letter:
                temptext[char] = switch
    message = ""
    for i in temptext:
        message += i
    return message


def leterFreq():
    order = ["e","t", "a"]
    return order


def replaceLetters(text, letter, replacement):
    temptext = list(text)
    for char in range(len(text)):
        if text[char] == letter:
            temptext[char] = replacement
    message = ""
    for i in temptext:
        message += i
    print(message)
    inp=raw_input("are you happy with the change? y/n\n")
    if inp == "y":
        return message
    else:
        return text


def openFile():
    file = open("CipherText/sub.txt","r").read()
    return file

file = openFile()
print(file)
subCipher(file)
