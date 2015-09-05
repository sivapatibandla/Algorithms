#-------------------------------------------------------------------------------------#
#------------------------------------- Introduction ----------------------------------#
#-------------------------------------------------------------------------------------#

print ("Assignment 1\n",
       "Course: Design and analysis of algorithms, part-1\n",
       "Author: Siva Patibandla\n",
       "Date: July 21 2015");

#-------------------------------------------------------------------------------------#
#------------------------------------- Functions -------------------------------------#
#-------------------------------------------------------------------------------------#

# Counts the number of inversions in the array in a brute force way
# Running time O(n^2)
def countInversions (numbers):
    inversionCnt = 0;
    for i in range (0, len (numbers)-1):
        print ("index i ", i);
        for j in range (i+1, len (numbers)):
            #print ("index i ", i, " j ", j);
            if (numbers[i] > numbers[j]):
                inversionCnt += 1;
    return inversionCnt;
        

# Sorts the array and counts the number of inversions using merge sort
# Running time O(nlogn)
def merge (left, right):
    leftIndex = rightIndex = 0;
    mergedOutput = [];
    global inversionCnt;

    while leftIndex < len (left) and rightIndex < len (right):
        #print ("left index: ", leftIndex, " left array: ", left,
               #" rightIndex: ", rightIndex, "right array: ", right);
        if left[leftIndex] < right[rightIndex]:
            mergedOutput.append(left[leftIndex]);
            leftIndex += 1;
        else:
            mergedOutput.append(right[rightIndex]);
            rightIndex += 1;
            # inversion between remaining elements of left (including the current element)
            # with the current element of right
            inversionCnt += len(left) - leftIndex; 
        
    while leftIndex < len (left):
        mergedOutput.append (left[leftIndex]);
        leftIndex += 1;
    while rightIndex < len (right):
        mergedOutput.append (right[rightIndex]);
        rightIndex += 1;
    #print ("Merged result: ", mergedOutput, " Curr inversion count: ", inversionCnt);
    return mergedOutput;

# Function which implements the divide and conquer step of the merge sort algorithm
def mergeSort (numbers):
    sortedLeft = sortedRight = [];
    size = len(numbers);
    #print ("size: ", size);
    if size == 1:
        #print ("returning: ", numbers);
        return numbers;
    left = numbers[:size//2];
    right = numbers[size//2:];
    sortedLeft = mergeSort (left);
    sortedRight = mergeSort (right);
    sortedNumbers = merge (sortedLeft, sortedRight);
    return sortedNumbers;

#-------------------------------------------------------------------------------------#
#------------------------------------- Main program ----------------------------------#
#-------------------------------------------------------------------------------------#
inversionCnt = 0;
numbers = [];
f = open ('IntegerArray.txt', 'r');
#f = open ('sample1.txt', 'r');
for line in f:
    numbers.append(int(line));
    #print (int(line));
print ("Input size: ", len(numbers));

sortedNumbers = mergeSort (numbers);
#print (sortedNumbers);
print ("inversion count merge sort: ", inversionCnt, " size: ", len(sortedNumbers));
#inversionCnt = countInversions(numbers);
#print ("inversion count brute force: ", inversionCnt);






