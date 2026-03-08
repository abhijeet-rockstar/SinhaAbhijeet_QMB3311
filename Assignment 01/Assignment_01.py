mport random as rm

a = rm.randrange(1,10)
print("Random Number is Generated : " ,a)
b = a*2
c = b+5
d = c*50


# My birthday in in the month of march
# I am writing this in march but my birthday is still ahead so i am adding 1750

#e = d+ 1750

# tried somthing new with the little help with AI

from datetime import datetime as dt

current_month = dt.now().month
if current_month == 3:
    e = d + 1750
else :
    e = d + 1749
print("My birthday is in march")


# this is 2026
#f = e + 26
current_year = (dt.now().year)%100
print("This is : 20",current_year)

f = e + current_year

g = f - 2004

print(g)
