"""58. Length of Last Word
Solved Easy
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal consisting of non-space characters only."""

def lengthOfLastWord(self, s):
      a=s.split()              #used split function to split the string into a list of separate words
      return len(a[-1])      #returned the length of the word in the last index of the list i.e the last word of the string
