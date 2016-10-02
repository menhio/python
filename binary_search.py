from time import time

#Determine whether collection contains target
def bs_contains(ordered, target):
    
    low = 0
    high = len(ordered) - 1
    
    while low <= high:
        mid = (low +  high) / 2
        if target == ordered[mid]:
            return True
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False

#Measure Performance
def performance():
    n = 1024
    while n < 50000000:
        sorted = range(n)
        now = time()
        
        bs_contains(sorted, -1)
        
        done = time()
        
        print n, (done-now) * 1000
        n *= 2
performance()
