[5,6,1,2,3,4,5]

def search_rotated(lst,elem):
    state=lst
    while state[0]:
        if lst[len(state)/2]==elem:
            return True
        elif lst[len(state)/2]>elem:
            if lst[len(state)/2] < lst[-1] :
                state=lst[len(state)/2+1:]
            else:


