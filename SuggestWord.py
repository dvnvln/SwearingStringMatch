import re
import bm
import kmp

def chooseAlgo(nama,word,badWords):
    if (nama=="kmp"):
        return (kmp(word,badWords))
    elif (nama=="bm"):
        return(bm(word,badWords))
    else:#nama == regex
        return (re.search(word,badWords))

def genPattern(word):
    return r"{}[a-z]+".format(word)

def findWord(masukan,kamus):
    result = re.findall(genPattern(masukan),kamus)
    return result

def suggestWord(blockOffense,words,badWords,algo):
    if (blockOffense):
        for word in words:
            isBad = chooseAlgo(algo,word,badWords)
            if(isBad):
                words.remove(word)
        return words
    else:
        return words

def main():
    bad = open("badwords.txt","r")
    rBad = bad.read()
    word = open("words.txt","r")
    rWord = word.read()
    wo = input("Type here : ")
    validasi = input("Block the offensive word? (yes/no) : ")
    if (validasi == "yes"):
        valid = True
    else:
        valid = False
    algo = input("waiiittt, what algo do u want to use? (kmp / bm (aka boyer moore) / regex) ")
    results = suggestWord(valid,findWord(wo,rWord),rBad,algo)
    print("These are the suggestion words :")
    for result in results:
        print(result)

if __name__ == '__main__':
    main()