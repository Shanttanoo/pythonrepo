# Assignment No: 2
# Define a function max() that takes two numbers as arguments and returns the largest of them.
# Use the if-then-else construct available in Python.
# (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)

def maxnum(a,b):
    if a<b:
        print str(b) + " is the larger number"
    elif b<a:
        print str (a) + " is the larger number"
    elif a==b:
        print "Both the numbers are equal"

x = input("Enter the first number: ")
y = input("Enter the second number: ")
maxnum(x,y)



