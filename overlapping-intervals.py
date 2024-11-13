def merge_intervals(intervals):

    #this will contain the merged intervals after checking them
    merged = [intervals[0]]
    
    #looping through the whole intervals except for the 1st one cus its already in the merged list
    for i in range(1, len(intervals)):
        # [-1] is the shortest way to get to the last element in the list 
        # so we're always comparing the last element we merged to the 1st element in the intervals of the ones that we didn't see yet to see if their times overlap 
        if(merged[-1][1] > intervals[i][0]):
            #max() is a built in function that gives the biggest value between numbers so it's a shortcut for using an if statement to check who's bigger
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            #appending the intervals right away cus they are not overlapping
            merged.append(intervals[i])
    #returning the merged intervals
    return merged

#printing the returned value from the merge_intervals function
print(merge_intervals([[1,3], [2,4], [6,8]]))