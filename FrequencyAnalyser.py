def analyser(inpt):
    key =  {"A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0, "I" : 0, "J" : 0, "K" : 0, "L" : 0, "M" : 0, "N" : 0, "O" : 0, "P" : 0, "Q" : 0, "R" : 0, "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0, }
    for char in inpt:
        val = int(ord(char))
        if (val <= 122) and (val >= 97):
            letter = val-32
            key[chr(letter)] += 1

        elif ((val <=90) and (val >= 65)):
            letter = val
            key[chr(letter)] += 1
    return key

def parse():
    f = open("CipherText/sub.txt", "r").read()
    freq = analyser(f)

def frequencyOrder(freq):
    order = []
    for i in range(26):
        letter = "-1"
        previous = -1
        for j in range(26):
            tLetter = chr(65+i)
            current = freq[tLetter]
            if current > previous:
                previous = current
                letter = tLetter
        order.append(letter)
        print(letter)
        freq[letter] = -1
    print (order)

f = open("CipherText/sub.txt").read()
freq = analyser(f)
frequencyOrder(freq)







parse()