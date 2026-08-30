"""258. Add Digits
Solved Easy
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it."""

def addDigits(self, num):
      num=str(num)      #converting to string for easy calculation
      a=0
      while len(str(num))>1:    #till the sum becomes a single digit the loop will keep running
          for i in num:        #assigning each digit as a char to i per loop
              a=a+int(i)        #adding the digits together
              num=str(a)          #storing the sum every loop in num so that while loop keeps running till it becomes a single digit sum
          a=0                  #assigning a=0 so that all sums dont get added together
      return int(num)              #the final sum i.e the one digit sum in str datatype will be returned as an integer
