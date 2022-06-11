# Find a triplet that sum to a given target

def triplats(array,target):
    for i in range(len(array)-1):
        s= set()
        curr_sum= target-array[i]
        for j in range(i+1,len(array)):
            if (curr_sum-array[j]) in s:
                print("triplates are: ",array[i], array[j], curr_sum-array[j])
                return True
            
            s.add(array[j])
    
    return False

        
    