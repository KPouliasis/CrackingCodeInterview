class QueueViaStacks():
    def __init__(self):
        self._s1=[]
        self._s2=[]
    def push(self,element):
        self._s1.append(element)
    def pop(self):
        if not self._s2:
            if self._s1:
                while self._s1:
                    cur=self._s1.pop()
                    self._s2.push(cur)
            else:
                raise IndexError
        el=self._s2.pop()
        return el