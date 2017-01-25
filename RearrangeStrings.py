# function determines if a string is different by one character
def isDiffByOne(s1, s2):
    # if the strings are equal, false
    if s1 == s2:
        return False

    # if a single char, they are different if not equal
    if len(s1) == 1:
        return True

    # else, we count differences in the string
    diffCount = 0
    # iterating over the string, if two chars are different, increment
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            diffCount += 1
    # if different by one, this count will only be one
    return diffCount == 1

# helper function that does the heavy lifting
def helper(rest):
    # if the length is 2, compare and return the list
    if len(rest) == 2:
        return (isDiffByOne(rest[0], rest[1]),rest)
    else:
        possible = False
        # for each item in the array, loop and try to see if the array is arrange-able
        for i in range(0, len(rest)-1):
            # the string we'll use to compare to the resultant array
            targetString = rest[i]
            # slice the array to exclude the target string
            tmp = rest[:i] + rest[i + 1:]
            # recursive call to try and fit this string
            (possible,tmp) = helper(tmp)
            # if the call returns true, try and fit the string somewhere within
            if possible:
                # loop over the modded array
                for j in range(0,len(tmp)):
                    # if first element fits, return true and insert the string in that position
                    if j == 0 and isDiffByOne(targetString,tmp[j]):
                        tmp.insert(0,targetString)
                        return (possible,tmp)
                    # if last element fits, append and return
                    if j == len(tmp)-1 and isDiffByOne(targetString,tmp[j]):
                        tmp.append(targetString)
                        return (possible,tmp)
                    # if the string fits somewhere in the middle, insert and return
                    if j < len(tmp)-1 and isDiffByOne(targetString,tmp[j-1]) and isDiffByOne(targetString,tmp[j+1]):
                        tmp.insert(j, targetString)
                        return (possible,tmp)
                # otherwise, return false -- it isn't possible
                return (False,tmp)
    # return final result
    return (possible,[])

# top-level routine
def stringsRearrangement(inputArray):
    return helper(inputArray)[0]

# main
if __name__ == "__main__":
    # run some tests
    print stringsRearrangement(["aaab","aaaa","aaac","xxxx","xxxc"]) # false
    print stringsRearrangement(["f", "g", "a", "h"]) # true
    print stringsRearrangement(["ef", "fe"]) # false
    print stringsRearrangement(["abc","abx","axx","abc"]) # false
    print stringsRearrangement(["ab","bb","aa"]) # true