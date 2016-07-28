class StackOfStacks():
    def __init__(self,capacity):
        self._contents=[]
        self._stack_capacity=capacity
        #self._cur_stack=
    def _current_size(self):
        return len(self._contents[-1])
    def push(self,elem):
        if self._current_size()<self._stack_capacity:
            self._contents[-1].append(elem)
        else:
            self._contents.append([elem])

    def pop(self):
        if self._contents:
            top=self._contents[-1][-1]
            if not self._contents[-1]:
                self._contents.pop()
            return top
        else:
            raise KeyError

    def top(self):
        return self._contents[-1].top()

    def adjust(self,i):
        if i == len(self._contents) and len(self._contents[i])==0:
            self._contents.pop()
        elif i==len(self._contents):
            return
        else:
            while self._contents[i+1]:
                helper=[]
                helper.append(self._contents[i+1].pop())
            self._contents[i].append(helper.pop())
            while helper:
                el=helper.pop()
                self._contents[i+1].append(el)

        return self.adjust(i+1)

    def pop_index(self,i):
        if i in range(len(self._contents)):
            if self._contents[i]:
                el=self._contents[i].pop()
                self.spill(i)
