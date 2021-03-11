# Problem 1
try:
    result = 5/0
except:
    print("You are dividing by 0!!")
    


# Problem 2
subjects = ['Americans', 'Indians']
verbs = ['play', 'watch']
objects = ['baseball', 'cricket']
for s in subjects:
    for v in verbs:
        for o in objects:
            print(s, ' ', v, ' ', o, '.', sep = '')