'''
j = 'January'
f = 'Febuary'
m = 'March'
a = 'April'
mm = "May"
ju = "June"
jl = "July"
au = "August"
s = "September"
o = "October"
n = "November"
d = "December"

print('Today is ' + f + ' 14th/2022 ' )
print('My younger sister birthday also is in ' + f + ". She is turning 18 this year. Time flys.")
print("My moms birthday is next month in " + m + ". I love my mom.")
print("My father birthday was last month in " + j + ". My father is gives me the best advice.")
print("Aunt TT birthday is in " + a + ". She is my favorite aunt. What is the date?")
x = input()

#slicing 

aa = "Hello World"
print(aa[2])

bb = "The rams just won the supper bowl"
print(bb[4])

cc = ("The only tv series on power I watch is power")
print(cc[0])

dd = "Good Day"
print(dd[5])

ee = 'Eagles next year'
print(ee[2])

ff = 'friday is a work day'
print(ff[7])

gg = 'goodness sake'
print(gg[3])

# looping string

for x in "football":
    print (x)

for mm in "Money and power":
    print(mm)

for ggg in "Good God Alamighty":
    print(ggg)

for zzz in "Zebras for breakfast":
    print(zzz)

for ccc in "Clowns are real":
    print(ccc)

for ttt in "I must have a job in teh before the end of the year":
    print(ttt)

for number in "1234567890":
    print(number)

for tea in "green black jeera moringa":
    print(tea)

for laptop in "hp & asus":
    print(laptop)

for ppp in "No loans ever again":
    print(ppp)

#length to get the length of a function use the len() function

print(len(aa))
print(len(bb))
print(len(cc))
print(len(dd))
print(len(ff))
print(len(gg))

# checking string
# To check if a certain string or charcter is present in a string, we use the keyword in

txt = "It dont matter if you enjoy it, just get it down"
print("Eagle" in txt)
print("matter" in txt)

txt2 = "What was the reason"
print("Cardi B" in txt2)
print("What was" in txt2)

txt3 = "James Harden is in Philly!"
print("Kyrie" in txt3)
print("Harden" in txt3)

if "James" in txt3:
    print("Yes we are the best team now")

if "reason" in txt2:
    print("Ok then")

if "enjoy" in txt:
    print("You are right")

print("Kyrie" not in txt3)
print("Iverson" not in txt2)
print("matter" not in txt)

if "Iverson" not in txt3:
    print("Hes the new PG now")

if "Python" not in txt2:
    print("Ok sir")
# more slicing
xx = "Hello World!"
yy = "Learning Python, Is Fun!"

print(xx[0])
print(xx[1])
print(xx[2])
print(xx[3])
print(xx[4])
print(xx[5])
print(xx[6])
print(xx[7])
print(xx[8])
print(xx[9])
print(xx[10])
print(xx[11])

#Slicing from the start
print(xx[:12])
print(xx[:11])

#slice to the end

print(xx[2:])


#Negative Indexing
print(xx[-5:-2])
print(xx[-2:])

#python modify string

print(xx.capitalize())
print(yy.upper())
print(xx.casefold())
print(xx.count('2'))

print(xx.lower())
print(yy.lower())

print("Today is a good day".lower())
print(" The rams one the superbowl yesterday. ".strip())

sep = "July"
print("Mandell birthday is in " + sep + " I need to get a gift.")

print(yy.replace("F", "G").lower())
print(yy.split(","))  # split() splits the string into sub stings
print(xx.split())

# concatenate
tt = "This is"
hh = "How we do it"
qq = tt + hh
print(qq)

print(tt + " " + hh.lower())

#Python format strings
# format() method takes the passed argument, formats them, and places them in the string where the placeholders {} are

age = 27

xxx = ("My name is Emmanuwil and I'm {}")
print(xxx.format(age))

'''
quantity = 90
itemno = 567
price = 39.99
myorder = "I want {} piecies of paper. {} for {} dollars"

print(myorder.format(quantity, itemno, price))

# index number are helpful for making sure arguments are in thr right place.
myorder1 = "I want to pay {2} dollars for {0} pieces of item. {1}"

print(myorder1.format(quantity, itemno, price))



