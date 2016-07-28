def urlify(word,length):
    index=0
    final=length-1
    while index<final:
        if word[index]== ' ':
            for i in range(final,index,-1):
                print word[i]
                word[i+2]=word[i]
            word[index:index+3]="%20"
            final+=2
        index+=1
    return word

print urlify(list("to mellon diarkei poly                       "),22)

