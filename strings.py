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
'''

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

