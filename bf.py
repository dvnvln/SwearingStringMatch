def bruteforce(pat,txt):
    m = len(pat)
    n = len(txt)

    for i in range (n):
        j = 0
        while ((j < m) and (txt[i+j] == pat[j])) :
            j+=1
        if (j == m):
            return True #match

    return False 
