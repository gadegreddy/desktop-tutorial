#{
x = range(100,200)
y = []
for x in x:
  if x%7 == 0 and x%5 != 0:
    y.append(x)
print(y)
#print(x,end=", ") without use of y !?

#Ex1 slicing

a = "python training"
print(a[3:4])

print(a[:4])

print(a[::-3])

#Ex2: range
for x in range(40,30,-3):
  print(x)
 
#string
#{
#ex1
name = "gk"
age =  36
print("i am %s and %d old" %(name,age))

#ex2
a = 22
b = 7
print("pi value is %.5f" %((a/b)))

#ex3
section = {"name" : "gk", "age" : 33}
print(section["name"])
print("i am %s and %d old" %(section["name"], section["age"]))



#ex4
x = input("your name: ") 
y = input("age: ")
class1 = dict({"name":x, "age":y})
print(class1)
print("i am %s and %s old" %(class1["name"], class1["age"]))





def plus(a,b):
    p = a+b
    print("sum of %d and %d is " %(a,b), p)
plus(a,b)
    
def minus(a,b):
    i = a-b
    print("subtraction of %d and %d is " %(a,b), i)
minus(a,b)

def multi(a,b):
    m = a*b
    print("multiplication of %d and %d is " %(a,b), m)
multi(a,b)

def div(a,b):
    d = a/b
    print("div of %d and %d is %.6f" %(a,b,d))
div(a,b)


#ex 1
def name(a,b):
    print("my full name is",f"\"{a}"<"{b}\"")
name(a = "gade", b = "kishore")

#ex 2
def square(a):
  return a*a
for i in [1, 2, 3]:
  x = square(i)
  print("square of",i,"is", x)


#ex 3
def add_numbers(a = 7.2, b = 8):
  sum = a + b
  print('Sum of %.1f and %d' %(a,b),"is", sum)
add_numbers(5, 4)
add_numbers(b=5)

#ex 4 
def test(*gk):
  for x,y in gk.items():
    print ("%s , %s" % (x, y))
test(x = "kishore", y = "thirty")

#eX5
num = 30
print("starting both function: ", num)
def out():
  num = 20
   
  def inv():
    global num
    num = 25
    print("Before calling in(): ", num)
  inv()
print("After calling in(): ", num)
#parallel ?    
out()

print("Outside both function: ", num)


def list_benefits():
  x = ("More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together")
  for benefit in x:
    print("%s is a benefit of functions!" % benefit)
list_benefits()

def list_benefits():
# keep the strings in () or [] make no diffrence
  return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
for benefit in list_benefits():
    print("%s is a benefit of functions!" % benefit)
list_benefits()

#
def division(a,b):
  return a/b
a = int(input("enter a: "))
b = int(input("enter b: "))
x = f'{division(a,b):.4f}'
#y = f'{x:.4f}' is same as above; y = round(x, 7) define x first
x = division(a,b)
#y =  is same as above
print(f'divison of {a} and {b} is {x}')
#print(f'divison of {a} and {b} is {division(a,b):.4f}')



def plus(a,b):
  return a+b
  
def minus(a,b):
  return a-b
  
def multiply(a,b):
  return a*b
  
def division(a,b):
  return a/b
  
a = int(input("enter a: "))
b = int(input("enter b: "))
x = plus(a,b)
y = minus(a,b)
z = multiply(a,b)
v = f'{division(a,b):.4f}'

print(f'addition of {a} and {b} is {x}')
print(f'substraction of {a} and {b} is {minus(a,b)}')
print(f'muliplication of {a} and {b} is {z}')
print(f'divison of {a} and {b} is {v}')


# input from the text file
with open("C:\Users\kishore.gade\Desktop\input.txt") as f:
  a = f.read()
print(f)