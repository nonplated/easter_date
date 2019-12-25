import math

def calculateEasterDate(year):
    '''
        for gregorian calendar
        method of Jean Meeus (https://en.wikipedia.org/wiki/Jean_Meeus)
        tested with https://www.assa.org.au/resources/more-articles/easter-dating-method/
    '''
    a = year % 19
    b = math.floor(year/100)
    c = year % 100
    d = math.floor(b/4)
    e = b % 4
    f = math.floor((b+8)/25)
    g = math.floor((b-f+1)/3)
    h = ((19*a)+b-d-g+15) % 30
    i = math.floor(c/4)
    k = c % 4
    l = (32+(2*e)+(2*i)-h-k) % 7
    m = math.floor((a+(11*h)+(22*l))/451)
    n = (h+l-(7*m)+114) % 31
    day = n+1
    month = math.floor((h+l-(7*m)+114)/31)
    return (year, month, day)
