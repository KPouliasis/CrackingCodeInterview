class QueueViaCircArray:
    def __init__(self,capacity):
        self._capacity=capacity
        self._size=0
        self._data = [None for i in range(capacity)]
        self._start=0
        self._end =0

    def is_full(self):
        return self._size==self._capacity
    def is_empty(self):
        return self._size==0

    def enqueue(self,elem):
        if self.is_full():

            self._data=self._data + [None for i in range(self._capacity,2*self._capacity)]
            self._capacity=len(self._data)

        self._data[self._end]=elem
        self._size+=1
        self._end=(self._end+1)%self._capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        else:
            el=self._data[self._start]
            self._data[self._start]=None
            self._start=(self._start+1)%self._capacity
            self._size-=1
            if self._size < self._capacity/4:
                if self._start<=self._end:

                    self._data=self._data[self._start:self._end] + [None for i in range(self._size,self._capacity/2)]
                    self._capacity=len(self._data)
                    self._start=0
                    self._end=self._size
                else:
                    self._data=self._data[self._start:]+self._data[self._end:self._start] + [None for i in range(self._size,self._capacity/2)]
                    self._data=len(self._data)
                    self._start=0
                    self._end=self._size
            return el

    def __repr__(self):
        if self._start<=self._end:
            return repr(self._data[self._start:self._end])
        else:
            return repr(self._data[self._start:]+self._data[self._end:self._start])
class StackAsDoubleQueue():
    def __init__(self):
        self._s1=QueueViaCircArray(10)
        self._s2=QueueViaCircArray(10)

        
    def push(self,element):
        self._s1.enqueue(element)

    def pop(self,element):
            if self._s1.is_empty():
                raise IndexError
            else:
                while not self._s1.is_empty():
                    cur=self._s1.dequeue()
                    if self._s1.is_empty():
                        val= cur
                    else:
                        self._s2.enqueue(cur)
                        while not self._s2.is_empty():
                            cur=self._s2.dequeue()
                            self._s1.enqueue(cur)
                return val




qu=QueueViaCircArray(10)
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(5)
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
print qu
