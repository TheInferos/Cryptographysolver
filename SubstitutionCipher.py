import FrequencyAnalyser

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
freq = FrequencyAnalyser.analyser(f)
frequencyOrder(freq)





