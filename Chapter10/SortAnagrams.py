def sort_anagrams(strarray):
    def compare(str1,str2):
        if sorted(str1)<sorted(str2):
            return -1
        elif sorted(str1)==sorted(str2):
            return 0
        else:
            return 1
    strarray.sort(cmp=lambda x,y: compare(x,y))
    return strarray

print sort_anagrams(["abba","bbaa","cat","moo","tac"])