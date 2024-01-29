# Python WHILE Loop - Compare User Input To Count Variable Lab
# Use this Replit to try some code... Use it as a scratch pad.

'''
Coding Challenge:
WHILE Loop - Compare User Input To Count Variable Lab

This Challenge is to write code that: 
Asks the user for an integer number 0 to 9 as input
Validate it's an integer (Hint: use your TRY/EXCEPT code)
Prints out the user input.  
Then use a while loop with a count variable, and loop from 0 to 10, and check when the user input variable matches the count variable.
When the user variable and the count variable are equal, print "The User variable is equal to the count variable. User = <the user variable value> Count variable = <the count variable>" 

Expected Output: If the user variable input was "6"
    Starting Code Challenge
6
Starting While Loop - Comparing User & Count Variable
0
1
2
3
4
5
The User variable is equal to the count variable. 
User = 6 
Count = 6
7
8
9
Starting While Loop
End Code Challenge

'''

# <Add Any Header Comments, Versioning & License>
# <Add a Comment Here to describe/explain what you are doing>

# Your Code Starts Here:
# Enter Your Code Here:

def main():
  print("Starting Code Challenge")
  try:
    x = int (input())
    
    print(x)
    print("Starting While Loop - Print Count Variable")
    count = 0
    while count < 11:
        if count == x:
            print ("The User variable is equal to the count variable. User = ", x , "Count variable = " , count)
            break
        print (count)
        count = count + 1;
  
  
    print("Ending While Loop")
    print("Ending Code Challenge")
  except:
    print ("Enter an INTEGER")


main()
