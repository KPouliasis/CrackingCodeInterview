def rev(word):
    word=list(word)
    for i in range(len(word)/2):
        word[i],word[-1-i]=word[-1-i],word[i]
    return word
print rev("lak")