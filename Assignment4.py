# Varun Kapoor
# Assignment 4


"""
1.1 Find the area of a Triangle using classes
"""
class Shape:
    def __init__(self):
        self.area = 0.0
        self.perimeter = 0.0
    def findArea(self):
        return self.area
    def findPerimeter(self):
        return self.perimeter
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
    def findArea(self):
        s = (self.a + self.b + self.c) / 2
        self.area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return self.area
    
"""
1.2 filter_long_words takes a list of words and an integer n and returns list of words longer than n
"""
def filter_long_words(lst, n):
    ret = []
    for elem in lst:
        if len(elem) > n:
            ret.append(elem)
    return ret

def filter_long_words_alt(lst, n):
    return list(filter(lambda word : True if len(word) > n else False, lst))

"""
2.1 Function that returns a list of the length of the strings inputted
"""
def length(words):
    ret = []
    for x in words:
        ret.append(len(x))
    return ret

def length_alt(words):
    return [len(x) for x in words]

"""
2.2 function that takes a character and returns True if a vowel
"""
def isVowel(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
           return True
    return False

def isVowel_alt(l):
    return True if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' else False











