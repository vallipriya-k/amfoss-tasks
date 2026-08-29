"""151. Reverse Words in a String
Solved Medium
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces."""

def reverseWords(self, s):
        a=s.split()                   #I used split function to separate the words from the string and assigned the list to a 
        b=""
        for i in range(len(a)-1,-1,-1):     #Used for loop to assign value of i from the index of the last string to the first in the list
            b=b+" "+a[i]                  #concatenated value of i which is a string each iteration to b with a space in the middle
        b=b.replace(" ","",1)            #the first concatenation would have created an unnecessary space infront of the string to get rid of it i used the replace function
        return b
