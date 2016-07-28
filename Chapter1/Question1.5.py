def compress(word):
    i=0
    acc=""
    while i<len(word):
        cur=word[i]
        counter=1
        next=i+1
        while next<len(word) and word[next]==cur:
            next+=1
            counter+=1
        acc+=('{}{}'.format(cur,counter))
        i=next
    return acc

print compress("aaannbccc")