def all_unique(input_string):
    freq_map=[ 0 ]*256
    for ch in input_string:
        freq_map[ord(ch)]+=1
    for freq in freq_map:
        if freq>1:
            return False
    return True

def all_unique_follow_up(word):
    wd=sorted(word)
    for i in range(len(word)-1):
        if wd[i]==wd[i+1]:
            return False
    return True
print all_unique_follow_up("kkko")
print all_unique_follow_up("alt")

