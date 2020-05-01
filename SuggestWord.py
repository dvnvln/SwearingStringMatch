import re
from bf import *
from bm import *
from kmp import *
import time

def chooseAlgo(nama,word,badWords):
    if (nama=="kmp"):
        return (kmp(word,badWords))
    elif (nama=="bm"):
        return(boym(word,badWords))
    elif (nama=="bf"):
        return(bruteforce(word,badWords))
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
    validasi = input("Block the offensive word? (y/n) : ")
    if (validasi == "y" or validasi == "Y"):
        valid = True
    else:
        valid = False
    print("what algo do you want to use?")
    algo = input("(bf(bruteforce)/kmp/bm(boyer moore)/regex) : ")
    start_time = time.time()
    results = suggestWord(valid,findWord(wo,rWord),rBad,algo)
    elapsed_time = time.time() - start_time
    print("These are the suggestion words :")
    for result in results:
        print(result)
    print ("Execution time : %.10f sec" % (elapsed_time))


if __name__ == '__main__':
    main()