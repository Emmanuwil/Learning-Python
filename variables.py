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
print(c)

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


#Outout Variables

x = "awesome"
print("python is " + x)


g = "Goku"  #ex1
print("Where is " + g + "?")

v = "Vegeta" #ex2
print("time for us to find that guy " + v)

gt = "Goten" #ex3
print(gt + " is the son of " + g)

t = "Trunks" #ex4
print(t + " & " + gt +" are close friends who love to spar.")

p = "Piccolo" #ex5
gh = "Gohan"
print(p +"'" + "s " + "1st friend was " + gh + ".")

w = "Whis" #ex6
b = "Beerus"
print(w + " is an angel" + " & " + b + " is a detroyer.")

j = "Jiren" #ex7
print(j + " is the strongest mortal alive.")

h = "Hit" #ex8
print(h + " is an assin who kills people. " + g + " even put a order for " + h + " to kill him.")

#ex9
print(g + " & " + v + " train with " + w + " so they can get godly power.")

#ex10
print(v + " will train with " + b + " seperatly so he can gey his own power.")

print(g, v + " & " + b +" are strong.")
# Global Variables

x = "great"  #ex1

def myfunc():
    print("Python is " + x)

myfunc()

c = "cool" #ex2

def my_func():
    print("Emmanuwil is " + c)

my_func()

b = "better" #ex3
def myfunction():
    print("Youngboy " + b)

myfunction()

py = "python" #4
def function():
    print("I love " + py)

function()

m = "moringa" #ex5
def newfunction():
    print("My favorite tea is " + m)

newfunction()

r = "regulated" #ex6
def function6():
    print("When I trade, I trade " + r)

function6()


d = "day" #ex7
def function7():
    print("I read for 30 mins a " + d)

function7()

l = "lion" #ex8
def function8():
    print("My favorite animal in the world is a " + l + ". The king of the jungle.")

function8()

lo = "lofi" #function9
def function9():
    print("When I study I like to listen to " + lo)

function9()

a = "Asus" #function10

def function10():
    print("In my opinion the best computer brand is " + a)

function10()

# variable inside a function, with the same name as th global variable.

x = "november"   #ex1

def globalfunction1():
    x = "11/26/1994"
    print("My birthday is " + x)

globalfunction1()

print("my birthday is in " + x)

e = "Elijah" #ex2
def globalfunction2():
    e = "Emmanuwil"
    print("My name is " + e)

globalfunction2()

print("My brother name is " + e)

p = "pizza"
def globalfunction3():
    p = "pinapples"
    print("I love bananas & " + p)

globalfunction3()

print("I like spinach on my " + p)

r = "Rod Wave" #ex4
def globalfunction4():
    r = "Rap"
    print("I like listening to " + r)

globalfunction4()

print("I like listening to " + r)

k = "Kyrie" #ex5
def globalfunction5():
    k = "kind"
    print("Its best to be " + k)
globalfunction5()

print("My guy " + k + " has the best handles in the NBA.")

b = "books" #ex6
def globalfunction6():
    b = "banks"
    print("I keep my money in credit unions not " + b)
globalfunction6()
print("Its very important that you keep your head in the " + b)

j = "JavaScript" #ex7
def globalfunction7():
    j = "jordans"
    print("When it comes to shoes I dont wear " + j)

globalfunction7()

print("When I become great at Python, I will become great at " + j)

rr = "React" #globalex8
def globalfunction8():
    rr = "Rolls Royce"
    print("I want an Acura NSX. I dont really care to have a " + rr)

globalfunction8()

print("I have every intention on learning " + rr)

s = "SQL" #ex9
def globalfunction9():
    s = "Sammy"
    print("I have a brother named " + s)

globalfunction9()

print("After I'm great at Python, JavaScript, Rust, and React I will must have great knowledge at " + s)

jj = "journal" #ex10
def globalfunction10():
    jj = "Jerry Jones"
    print(jj + " is a billionare")

globalfunction10()

print("2022 I " + jj + " every week.")

# the global keyword

from glob import glob


def myfunc(): #ex1
    global x
    x = "amazing"

myfunc()

print("Python is " + x)

def myfunc2(): #ex2
    global k
    k = "king"

myfunc2()
print("Simba is the " + k)

def myfunc3(): #ex3
    global i
    i = "Iphone"

myfunc3()
print("The phone I have is an " + i)


def myfunc4(): #ex4
    global c
    c = "Chronixx"

myfunc4()
print("I enjoy listening to the reggea artist " + c)

def  myfunc5(): #ex5
    global a
    a = "Alkaline"

myfunc5()
print("The Best dancehall artist is " + a)

def myfunc6(): #ex6
    global l
    l = "love"

myfunc6()
print("Im completly focused on work. Not " + l)


def myfunc7(): #ex7
    global w 
    w = "water"

myfunc7()
print("The only drink you should drink everyday is " + w)

def myfunc8(): #ex8
    global s
    s = "sunday"

myfunc8()
print("The super bowl is this " + s)


def myfunc9(): #ex9
    global t 
    t = "time"

myfunc9() 
print("The most valuable asset that we have on earth is " + t)

def myfunc10():
    global g
    g = "glasses"

myfunc10()
print("I have terrible vision without my " + g)
"""

#changing the global variable inside a function, refer to the variable by using the global Keyword.




x = "awesome"

def myfunc(): #ex1
    global x
    x = "excellent"

myfunc()

print("Learning Python is" + x)

d = "diamonds"  #ex2
def myfunc22():
    global d
    d = "doomsday"

myfunc22()
print("superman cant beat " + d)

h = "happy" #ex3
def myfun33():
    global h
    h = "health"

myfun33()
print("money is cool in all but whats more importnat than that is " + h)

v = "vaction" #ex4

def myfunc44():
    global v
    v = "victory"

myfunc44()
print("I've lost a few battles recently, but I will see " + v)

e = "Eagles" #ex5
def myfunc55():
    global e
    e = "education"

myfunc55()
print("I love watching sport but right now its all about my " + e)

p = "power" #ex6
def myfunc66():
    global p
    p = "principle"
    
myfunc66()

print("As a man you need to stand on your " + p)

mi = "major" #ex7
def myfunc7():
    global mi
    mi = "Michael"

myfunc7()

print("My middle name is " + mi)


j = "jackson" #ex8
def myfunc88():
    global j
    j = "jackket"

myfunc88()
print("The gift that one of my friends gave me was a " + j)


f = "resistance" #ex9
def myfunc99():
    global f
    f = "forgive"

myfunc99()
print("The best thing you do as a human is " + f)

xx = "exercise" #ex10

def myfunc100():
    global xx
    xx = "Hvac"

myfunc100()
print("I will combine my skills in tech with " + xx)


