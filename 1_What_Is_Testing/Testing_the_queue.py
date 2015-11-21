# CORRECT SPECIFICATION:
#
# the Queue class provides a fized-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer >0 that
# is the maximum number of elements the queue can hold
#
# empty() returns True iff the queue holds no elements
#
# full() returns True iff the queue cannot hold any more elements
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty
#
# Modified by Thiago Figueiró at 21/11/2015 00:00
# - Completed test2: tests the 'enqueue' method
# - Completed test3: tests the 'dequeue' method

import array

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x


def test1():
    q = Queue(3)
    res = q.empty()
    if not res:
        print "test1 NOT OK"
        return
    res = q.enqueue(10)
    if not res:
        print "test1 NOT OK"
        return
    res = q.enqueue(11)
    if not res:
        print "test1 NOT OK"
        return
    x = q.dequeue()
    if x != 10:
        print "test1 NOT OK"
        return
    x = q.dequeue()
    if x != 11:
        print "test1 NOT OK"
        return
    res = q.empty()
    if not res:
        print "test1 NOT OK"
        return
    print "test1 OK"

def test2():
    
    print "testing the 'enqueue' method"
    beta = Queue(5)
    beta.enqueue(3)
    
    if beta.size != 1:
        print "test2 NOT OK err 1"
        return
    if beta.data[beta.tail] != 1:
        print "test2 NOT OK err 2"
        return    
    if beta.tail != 1:
        print "test2 NOT OK err 3"
        return       
    beta.enqueue(3)
    if beta.size != 2:
        print "test2 NOT OK err 4"
        return
    if beta.data[beta.tail] != 2:
        print "test2 NOT OK err 5"
        return    
    if beta.tail != 2:
        print "test2 NOT OK err 6"
        return      
    print "test2 OK"
    
def test3():
    print "testing the 'dequeue' method"    
    charlie = Queue(5)   
    charlie.enqueue(3)
    charlie.enqueue(3)
    charlie.dequeue()
    if charlie.size != 1:
        print "test3 NOT OK err 1 "
        return
    if charlie.data[charlie.tail] != 2:
        print "test3 NOT OK err 2"
        return    
    if charlie.tail != 2:
        print "test3 NOT OK err 3"
        return      
    print "test3 OK"
test1()
test2()
test3()
