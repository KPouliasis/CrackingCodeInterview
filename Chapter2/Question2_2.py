def find_kth(llist,k):
    forward=llist
    steps=0
    while forward and steps<k:
        forward=forward.next
        steps+=1
    if not forward:
        return llist
    back=llist
    while forward:
        back=back.next
        forward=forward.next
    return back

