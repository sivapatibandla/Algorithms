#-------------------------------------------------------------------------------------#
#------------------------------------- Introduction ----------------------------------#
#-------------------------------------------------------------------------------------#

print ("Assignment 2\n",
       "Course: Design and analysis of algorithms, part-1\n",
       "Author: Siva Patibandla\n",
       "Date: Aug 2 2015");

#-------------------------------------------------------------------------------------#
#------------------------------------- Globals ---------------------------------------#
#-------------------------------------------------------------------------------------#

from enum import Enum;
import sys;

class PivotType (Enum):
    FIRST = 1;
    LAST = 2;
    MEDIAN = 3;
    MEDIAN_AUTO = 4;

numbers = [];
comparisons = 0;

rule = PivotType.FIRST;

#-------------------------------------------------------------------------------------#
#------------------------------------- Functions -------------------------------------#
#-------------------------------------------------------------------------------------#

# This function returns the index of the pivot
def choosePivot (rule, start, end):
    if rule == PivotType.FIRST:
        return start;
    if rule == PivotType.LAST:
        return end;
    if rule == PivotType.MEDIAN:
        middle = start + (end-start)//2;
        subset = [];
        subset.append ([start, 0]);
        subset.append ([middle, 0]);
        subset.append ([end, 0]);
        
        mean = (numbers[start] + numbers[middle] + numbers[end])/3;
        least = sys.maxsize;
        leastIndex = 0;
        for i in range(0,3):
            subset[i][1] = abs(numbers[subset[i][0]] - mean);
            if subset [i][1] <  least:
                least = subset[i][1];
                leastIndex = subset[i][0];
        #print ("start ", start, " middle ", middle,
               #" end ", end, " mean ", mean, " subset ", subset);
        return leastIndex;
    if rule == PivotType.MEDIAN_AUTO:
        subset = [];
        middle = start + (end-start)//2;
        subset.append (numbers[start]);
        subset.append (numbers[middle]);
        subset.append (numbers[end]);
        subset.sort();
        medianIndex = numbers.index (subset[1]);
        #print ("start ", start, " middle ", middle,
               #" end ", end, " least index ", medianIndex, " subset ", subset);
        return medianIndex;
            

def swap (index1, index2):
    global numbers;
    temp = numbers[index1];
    numbers[index1] = numbers[index2];
    numbers[index2] = temp;

def quickSort (start, end):

    global numbers, comparisons, rule;

    # if the length of the array is 1 then exit
    # less than 0 covers a case where rightStart will be equal to end+1.
    # possible if left most element of x is the largest
    if end-start <= 0:
        return;
    else:
        comparisons += end - start;
    # Switch first element of the array with the pivot
    pivotIndex = choosePivot (rule, start, end);
    swap (start, pivotIndex);
    pivot = numbers[start];
    #print ("start ", start, " end ", end, "pivot ", numbers[start]);

    # Start comparing from the 2nd element,
    # as the first one is the pivot element
    rightStart = start+1;   
    for unseen in range (rightStart, end+1):
        if numbers[unseen] < pivot:
            swap (rightStart, unseen);
            rightStart += 1;
            #print ("unseen ", unseen, " swapped: ", numbers, " right start: ", rightStart);

    swap (start, rightStart-1);

    #print ("post swaps: ", numbers);

    quickSort (start, rightStart-2);
    quickSort (rightStart, end);

#-------------------------------------------------------------------------------------#
#------------------------------------- Main program ----------------------------------#
#-------------------------------------------------------------------------------------#

#f = open ('sample.txt', 'r');
f = open ('QuickSort.txt', 'r');
for line in f:
    numbers.append (int(line));
    
#print (numbers);

rule = PivotType.MEDIAN_AUTO; 
quickSort (0, len(numbers)-1);

print ("sorted Numbers:\n", numbers);
print  ("Comparisons ", comparisons);
