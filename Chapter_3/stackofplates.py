class StackofPlates():
    def __init__(self,capacity):
        stack_list=StackofPlates(capacity)
        self._stacks=[stack_list]
        self._size=1
        self._capacity=capacity
    def push(self,element):
        if self._stacks and len(self._stacks[self._size-1]) < self._stacks[self._size-1]._capacity:
            self._stacks[self._size-1].push(element)
        elif len(self._stacks[self._size-1]) >= self._stacks[self._size-1]._capacity:
            new_stack=StackState(self._capacity)
            new_stack.push(element)
            self._stacks.push(new_stack)
            self._size+=1
        else:
            raise IndexError

    def pop(self):
        if self._size and self._stacks[self._size-1]._size>0:
            el=self._stacks[self._size-1].pop()
            if self._stacks[self._size-1]._size==0:
                self._stacks[self._size-1]=None
                self._size-=1
        else:
            raise IndexError





class StackState():
    def __init__(self,capacity):
        self._capacity=capacity
        self._size = 0
        self._data=[None for i in range(capacity)]
    def push(self,element):
        if self._size<self._capacity:
            self._data[self._size]= element
            self._size+=1
        else:
            raise IndexError
    def pop(self):
        if self._size:
            el=self._data[self._size-1]
            self._data[self._size-1]=None
            self._size-=1
            return el
