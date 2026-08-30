"""231. Power of Two
Solved Easy
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x."""

def isPowerOfTwo(self, n):
      a=0
      if n<1:
          return False
      else:
          while n>1:
              if n%2==0:                        #checking if n divisible by 2
                  n=n/2                         #if yes it will keep dividing untill it isn't anymore
              else:
                  a+=1                          #this will help in returning True if it is a number that is divisible by 2
                  return False                  #since the num can't be divided by 2 completely till it becomes 1 it is not a power of 2  
          if a==0:                              #if a was increased by 1 it woould have been False if its not its True
              return True
