# for loop - O(n) Time, O(1) space

def ValidateSequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break 
# we've set a variable to 0 and set up a for loop to go through each value in the array.
# the if statement states if the variable 'seqIdx' is the same as the length of the sequence, break out of the loop and return TRUE (line15).
        if sequence[seqIdx] == value:
            seqIdx +=1 
# if the integer at index 0 is equal to the value of the sequence '1'. Add integer to the variable (seqIdx) by 1. This will make seqIdx = 1 and will index to the next integer.
# Remember the loop will keep looping until the seqIdx = the len(sequence)[4] 
    return (f"All the numbers in the sequence are in the array\nThis a {seqIdx == len(sequence)} statement")
# this will return as a boolean - true or false, once the loop has finished.

result = ValidateSequence([5,1,22,25,6,-1,8,10],[1,6,-1,10])
print(result)