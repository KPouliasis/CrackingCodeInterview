def replace_spaces(word):
    return 'some'.join(word.split())

print replace_spaces("asd ad a  daad adad adda ddddda")

def replace_alt(word):
    acc=[]
    i=0

    while i<len(word):
        cur=i
        while  cur<len(word)  and  word[cur]!=' ':
            cur+=1
        acc.append(word[i:cur])
        i+=1
    if acc:
        res=acc[0]
    for subs in acc:
        res+=subs
    return res

print replace_alt(" al;kdf  afdf afd fadf  fsdaf d  adfdafda fdafd  dfd ffd fff")
