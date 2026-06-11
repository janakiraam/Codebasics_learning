'''def volu_cylider(radius, height):
    volume = 3.14*(radius**2)*height
    return volume

volume=volu_cylider(2,3)
print(volume)
'''

### args and Kwargs

def sum(*args):
    total = 0
    for n in args:
        total+=n
    return total

def keywordarg(**kwargs):
    if 'ticker' in kwargs:
        print("ticker:", kwargs['ticker'])
def all_keywordarg(**kwargs):
    for key in kwargs:
        print(key,":",kwargs[key])

j=sum(4,5,67,4)
print(j)

m=keywordarg(ticker = 'test', ceo = 'rain', CTO = 'vembu')
m=all_keywordarg(ticker = 'test', ceo = 'rain', CTO = 'vembu')


##lamabda function for a function 
#def squ(a):
#a*a

x = lambda a : a*a
print(x(5))

