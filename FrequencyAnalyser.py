def analyser(inpt):
    value = []
    for i in range (26):
        value.append(0)
    total = 0
    for char in inpt:
        val = int(ord(char))
        if (val <= 122) and (val >= 97):
            letter = val-97
            value[letter] += 1
            total += 1
        elif ((val <=90) and (val >= 65)):
            letter = val - 65
            value[letter] += 1
            total += 1
    message = ""
    for i in range (26):
        message += str(chr(65+i)) + " = " + str(value[i]) + " "
    print message
    print total

def parse():
    f = open("CipherText/sub.txt", "r").read()
    analyser(f)

parse()