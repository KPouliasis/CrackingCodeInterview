def one_zero_away(wd):
    closure=set()
    chars= (chr(ord('a')+i) for i in range(26))
    for char in chars:
        for i in range(len(wd)):
           closure.add(wd[:i]+char+wd[i:])
           closure.add(wd[:i]+wd[i+1:])
           closure.add(wd[:i]+char+wd[i+1:])
    return closure

print one_zero_away("yolo")