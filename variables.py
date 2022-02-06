"""
myvar = "Emmanuwil"
my_var = "Emmanuwil"
_my_var = "Emmanuwil"
myVar = "Emmanuwil"
MYVAR = "Emmanuwil"
myvar2 = "Emmanuwil"

myVariableName = "EmmanuwilSimon"
MyVariableName = "EmmanuwilSimon"
my_variable_name = "EmmanuwilSimon"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print(myVariableName)  #Camel case
print(MyVariableName)  #Pascal case
print(my_variable_name) #Snake case


# Python Varible - Assign Multiple Varibles

x, y, z = "Python", "Javascript", "Rust"

print(x)
print(y)
print(z)

#One Value to multiple variables

a = b = c = "Orange"

print(a)
print(b)
print(c)"""

#Unpack a collection

sports = ["football", "basketball", "soccer"]
d, e, f, = sports
print(d)
print(e)
print(f)


colors = ["blue", "red", "green"]
g, h, i = colors
print(g)
print(h)
print(i)


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
mon, tue, wed, thur, fri = weekdays
print(mon)
print(tue)
print(wed)
print(thur)
print(fri)

currencies = ["British Pound/U.S Dollar", "Australian Dollar/U.S Dollar", "Euro/Austrian Dollar"]
GBPUSD, AUSUSD, EURAUD = currencies
print(GBPUSD)
print(AUSUSD)
print(EURAUD)

Family = ["Father", "Mother", "Brother", "Sister"]
Dad, Mom, Bro, Sis = Family
print(Dad)
print(Mom)
print(Bro)
print(Sis)

Cars = ["Acura", "Honda", "Jeep"]
nsx, Accord, Wrangler = Cars
print(nsx)
print(Accord)
print(Wrangler)

Tea =["Moringa", "White", "Soursop"]
o, p, i = Tea
print(o)
print(p)
print(i)

DBZ = ["Goku", "Vegeta", "Gohan", "Trunks", "Goten"]
hero, warrior, noble, tough, student = DBZ
print(hero)
print(warrior)
print(tough)
print(student)


rappers = ["NBA Youngboy", "Drake", "Lil Wayne", "Eminem", "2pac"]
Top, Drizzy, Weezy, Shady, Pac = rappers
print(Top)
print(Drizzy)
print(Weezy)
print(Shady)
print(Pac)

App = ["Facebook", "Instagram", "Twitter"]
Book, IG, Bird = App
print(Book)
print(IG)
print(Bird)