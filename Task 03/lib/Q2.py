"""78. Subsets
Solved Medium
Given an integer array nums of unique elements, return all possible (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order."""

def subsets(self, nums):
        l=[]
        for i in range(len(nums)+1):                    #looping no of times no of elemnts are in the list
            a=list(itertools.combinations(nums,i))      #Used itertools.combination() function to create subsets of nums list with i elements every loop
            lis= [list(item) for item in a]            #the previous function would result in a list of tuples to convert it back to lists list comprehension is used
            l=l+lis                                     #the list assigned to lis is concatenated to l every loop
        return l
