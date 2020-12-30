# Varun Kapoor
# Assignment 3

""" 
1.1 Function that works like python's reduce()
"""

def myreduce(func, seq):
    for x in seq:
        func(x)
    return

"""
1.2 Function that works like python's filter()
"""

def myfilter(func, seq):
    ret = []
    for a in seq:
        if func(a):
            ret.append(a)
    return ret

"""
2. List Comprehension
"""

# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
list1 = [ item for a in [ [x, x*2, x*3, x*4] for x in ['x','y','z'] ] for item in a ]

# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
list2 = [ item*i for i in [1,2,3,4] for item in ['x','y','z'] ]

# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
list3 = [ [item+i] for item in [2,3,4] for i in [0,1,2]]
list4 = [ [item+i for item in [2,3,4,5]] for i in [0,1,2,3] ]

# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
list5 = [ (a,b) for b in [1,2,3] for a in [1,2,3]]














