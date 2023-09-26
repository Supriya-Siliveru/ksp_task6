print("Hello!") #print statement

# single line comments
# or """  """ - multiline comments

# variables and data types

number = 5 #int
country = "Bharat" #string
decimalNumber = 9.5 #float
# boolean - true , false

# changing datatypes

print(type(number)) #output:- class 'int'

print(float(number)) #5.0 -int is changed to float

print(int(decimalNumber)) #9 float to int

# string methods

txt = "hii guys this is supriya"
txt1 =txt.capitalize()
print(txt1) 

newtxt = "Hii Guys"

txt2 = newtxt.casefold()
print(txt2)

txt3 = newtxt.center(20)
print(txt3)

txt4 = txt.count('i',5,15)
print(txt4)

x = "My name is Ståle"

txt5 = x.encode()

print(txt5)

txt6=x.endswith('E') 
print(txt6) #false

txt7 = x.startswith('M')
print(txt7)

y = "H\te\tl\tl\to"

txt8 =  y.expandtabs(5)

print(txt8)

txt9=txt.find("this")
print(txt9)

rightfind=txt.rfind("s")
print(rightfind)

z="{some} apples"
txt10 = z.format(some = 5)
print(txt10)

indexvalue = z.index('p')
print(indexvalue)

rightindex=z.rindex('m')
print(rightindex)

alphanumeric = z.isalnum()
print(alphanumeric)

alpha= z.isalpha()
print(alpha)

ascii= z.isascii()
print(ascii)

d="24"
decimal= d.isdecimal()
print(decimal)

digit= d.isdigit()
print(digit)

identifier = z.isidentifier()
print(identifier) #identifier cannot start with a number or cannot contain any spaces

lowerornot=txt.islower()
print(lowerornot)

lower = newtxt.lower()
print(lower)

numeric=d.isnumeric()
print(numeric)

c= "Hello! @1"
printable=c.isprintable()
print(printable)

space= c.isspace()
print(space)

titleornot=c.istitle()
print(titleornot)

title = c.title()
print(title)

upperornot=c.isupper()
print(upperornot)

upper =txt.upper()
print(upper)

myTuple = ("career", "X", "club")

e = "#".join(myTuple)

print(e)

sample ="Manali"

f = sample.ljust(8)
print(f, "is my fav place.")

g = sample.rjust(8)
print(g, "is my fav place.")

car = "       Rolls Royce      "
stripping = car.strip()
print(stripping)

leftstripping = car.lstrip()
print(leftstripping)

rightstripping = car.rstrip()
print(rightstripping)

partition=txt.partition("is")
print(partition)

sample2= "I eat apples daily, apples are good for health"
rightpartition=sample2.rpartition("apples")
print(rightpartition)

split=txt.split()
print(split)

splitlines=txt.splitlines()
print(splitlines)

sample3=("cricket, volleyball, badminton")
rightsplit=sample3.rsplit(",")
print(rightsplit)

swap=sample2.swapcase()
print(swap)

i="10"
zfilling=i.zfill(5)
print(zfilling)

sample4="I like Manali"
replacing=sample4.replace("Manali", "Kerala")
print(replacing)

sample5= "Hello Sam!"
mytable = str.maketrans("S", "P")
print(sample5.translate(mytable))

# function with arguments and parameters

def language(name):
    print("I Speak "+ name)
language("English")
language("Telugu")  #name- parameter, English and Telugu are arguments

def multi( num1,num2):
    print(num1 * num2)
multi(65,98)
