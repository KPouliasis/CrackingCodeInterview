class StackWithMin():
    def __init__(self,capacity):
        self._l1=[]
        self._l2=[]
        self._capacity=capacity
        self._size = 0

    def push(self,element):
       self._l1.append(element)
       if self._l2 and self._l2[-1]>=element:
           self._l2.append(element)
       if not self._l2:
           self._l2.append(element)
    def pop(self):
        if not self._l1:
            raise IndexError
        else:

            el=self._l1.pop()
            if el == self._l2[-1]:
                self._l2.pop()
            return el

    def __repr__(self):
        return self._l1.__repr__()


