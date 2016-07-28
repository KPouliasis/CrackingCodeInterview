# Nice problem
import operator
class Three_stack():
    def __init__(self,number_of_stacks,default_size):
        self._info = [None for i in range(number_of_stacks)]
        for i in range(number_of_stacks):
            self._info[i]= StackInfo(default_size*i,default_size)
        self._data=[None]*(number_of_stacks*default_size)

    def within_stack_capacity(self,index,at):
        start,capacity = self._info[at]._start, self._info[at]._capacity
        if index<0 or (index >= len(self._data)):
            return False
        if index < start:
            return index < (start +  capacity)% len(self._data)
        return index< start + capacity

    def adjust_index(self,index):
        max=len(self._data)
        return ((index % max) + max) %max

    def last_capacity_index(self,at):
        start,capacity = self._info[at]._start, self._info[at]._capacity
        return self.adjust_index(start+capacity-1)

    def last_element_index(self,at):
        start,size = self._info[at]._start, self._info[at]._size
        return self.adjust_index(start+size -1)

    def next_index(self,index):
        return self.adjust_index(index+1)

    def previous_index(self,index):
        return self.adjust_index(index-1)

    def is_fulll(self,at):
        return self.last_capacity_index(at) == self.last_element_index(at)

    def is_empty(self,at):
        size=self._info[at]._size
        return (size == 0)

    def shift_and_shrink(self,at):
        start=self._info[at]._start
        if not self.is_fulll(at):
            index=self.last_capacity_index(at)
            while self.within_stack_capacity(index,at):
                self._data[index]=self._data[self.previous_index(index)]
                index = self.previous_index(index)
            self._data[start]=0
            self._info[at]._capacity -=1
            self._info[at]._start= self.next_index(start)

        else:
            self.shift_and_shrink((at+1)%len(self._info))
            self._info[at]._capacity+=1

    def expand(self,at):
        if not self.is_fulll(at):
            self._info[at]._size+=1
        else:
            self.shift_and_shrink((at+1)%len(self._info))
            self._info[at]._size+=1

    def all_full(self):
        return reduce(operator.__and__,(self.is_fulll(i) for i in range(len(self._info))),True)

    def push(self,at,element):
        if self.all_full():
            raise IndexError
        else:
            self.expand(at)
            self._data[self.last_element_index(at)]=element

    def pop(self,at):
        el=self._data[self.last_element_index(at)]
        self._info[at]._size -=1
        return el





class StackInfo():
    def __init__(self,start,capacity,size):
            self._size=size
            self._start=start
            self._capacity=capacity


