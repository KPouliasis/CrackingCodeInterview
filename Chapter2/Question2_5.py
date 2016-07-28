def add_linked(fst,snd):
    def state_update(state,val):
        nd=__Node(val)
        hd,tail=state
        tail.next=nd
        return (hd,nd)
    class __Node():
        def __init__(self,val=0):
            self._val=val
            self._next=None


    res=None
    cur1,cur2=fst,snd
    curry_over=0
    pos=0
    while cur1 and cur2:
        res_value=((cur1.val+cur2.val+curry_over)%10)
        nd=__Node(res)
        if not res:
            res=(nd,nd)
        else:
            res=state_update(res,res_value)

        curry_over=(cur1.val+cur2.val+curry_over)/10
        cur1,cur2=cur1.next,cur2.next
    cur=cur1 if cur1 else cur2
    while cur:
        res=state_update(res,cur.val)
        cur=cur.next

    return res[0]

