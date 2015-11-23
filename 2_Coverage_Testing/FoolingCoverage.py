# SPECIFICATION:
#
# The stats function computes some basic statistics functions
# when given a list of numbers as input.
#
# TASK:
#
# Achieve full statement coverage on the stats function. 
# You will need to:
# 1) Insert a bug into the stats function.
# 2) Modify test1 so that it still achieves full test 
#    coverage, but does not trigger your bug. Depending 
#    on the bug you insert, you may not need to modify 
#    test1 at all.
# 3) Write test2 so that it also achieves full test 
#    coverage, but does trigger your bug.
#
# Modified by Thiago Figueiró at 23/11/2015
# - "Broke" program at line 42
# Put "median = (lst_sorted[middle+1] + lst_sorted[middle-1]) / 2" 
# when the correct is "median = (lst_sorted[middle] + lst_sorted[middle-1]) / 2" (Notice the first lst_sorted)
# Now the Median will return a wrong number.
#

import math

# Insert a bug of your choosing into the stats function.
def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lst_sorted = sorted(lst)
    if len(lst_sorted)%2 == 0:
        middle = len(lst_sorted)/2
        
        # BUG ALERT! 
        median = (lst_sorted[middle+1] + lst_sorted[middle-1]) / 2
        # BUG ALERT! 

    else:
        median = lst_sorted[len(lst_sorted)/2]
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append (num)
    print "list = " + str(lst)
    print "min = " + str(min)
    print "max = " + str(max)
    print "median = " + str(median)
    print "mode(s) = " + str(mode)

# test1 should achieve full statement coverage of 
# the stats function without triggering the bug 
# you've inserted into the stats function.
def test1():
    ###Your test1 code here. Depending on what 
    # bug you choose to put in the stats function, 
    # you may or may not need to modify test1.
    l = [1,2,3]
    stats(l)
    
    m = [1,2,3,4]
    stats(m)
    
    z = [0,0,0,0,0,0,0]
    stats(z)
    
# test2 should also achieve full statement coverage 
# of the stats function, but should trigger the bug 
# you've inserted into the stats function.
def test2():
    l = [0,-1,-2,-3,-3,-2,-6]
    stats(l)
    
    l = [1,99999,3,4]
    stats(l)
    pass

test1()
test2()

