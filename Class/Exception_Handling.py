'''
x=input("Enter the number 1: ")
y=input("Enter the number 2: ")

d=int(x)/int(y)

print(d)

'''

# exception handling with simple technique
'''
x=input("Enter the number 1: ")
y=input("Enter the number 2: ")

d=0

try:
    d=int(x)/int(y)
except:
    print("exception occured and handled")
    d=-1

print(d)

'''

## defining a proper exception

x=input("Enter the number 1: ")
y=input("Enter the number 2: ")



try:
    d=int(x)/int(y)
    j="raam"+31
# except ZeroDivisionError as Ze:
#     print("exception occured",Ze)
#     d=-1

# except TypeError as ted:
#     print("exception occured: ",ted)
#     d=-1

except Exception as e:  # this is a generic exception use to execute and capture any expection. Not recommended to use
    print("generic exception is captured: ", e)
    d=-1

finally:              #this finally block execute at every condition.
    k=2+3
    print("finally block executed and value of k is: ", k)

print(d)

# understand about raise ValueError() function to raise a exception.