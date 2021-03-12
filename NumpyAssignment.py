# Problem 1
def powervector(arr):
    ret = []
    for x in range(len(arr)):
        ret.append(arr[x] ** (len(arr)-x-1))
    return ret

# Problem 2
def moving_average(arr, window):
    ret = []
    for i in range(len(arr)-window+1):
        val = sum(arr[i:i+window])/window
        ret.append(val)
    return ret