'''
first_name = "gade"
second_name = "kishore"
full_name = first_name + " "+ second_name
print(full_name.title())
h = "hi!"
message = f"{full_name.title()}"
print("Hi! "f"{full_name.title()}")
print("Hi!",f"{full_name.title()}")
print (f"{h.title()} {full_name.title()}")





author = "gk"
q= "\"try hard\"  "
quote =("%s %s") %(author,q)

print(quote)
print(author,"said that",q)
print(author,"said that",q)
print(author," "+quote)
print("%s" %(author),"said that",("%s")%(q))
print("%s Said that %s" %(author.strip(),q.strip()))

age = {"gk": 35, "GGR": 70}
print(age["gk"])
print(age["GGR"])


def name():
    global x
x = "gk"
name()
print(x)

name = "gk"
age = 39
print("my name is %s and age is %s" %(name,age))
x = 3.1234566
print("numbers %.3f" %(x))

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string, data[0],data[1],"your current balance is $",data[2],".")
print(format_string,"%s %s. your current balance is $%s." %("John","Doe",53.44))
print(format_string, "%s %s. your current balance is $%s." %(data))



astring= "abcdefg"
print(astring[1:4:2])
print(astring.index("c"))


astring = "Hello world!"
print(astring.startswith("H"))
print(astring.endswith("!"))

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[0::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

>>> simple_url = nostarch_url.removeprefix('https://')
like removeprefix() in URL addressbar.

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)
motorcycles[0].append('ducati')

print(motorcycles)


ab = "Excelra"
print(ab[-1]+ab[1:-1]+ab[0])

# change this code
number = 20
second_number = 10
first_array = [1, 2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array[1] ==2:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number < 5:
    print("6")


loops list
for while pass else 

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)


a = 22

while a < 33:
    if a == 26:
        break
    a += 1
    print(a)

a = 22
b = 11
print(b,"is less than",a) if b<a else("b is greter than a")

year = 2001
if year%4 == 0 or year%400 == 0: print(year,"is a leaf year")
else: print(year, "not a leaf year")
year = 2022


for year in range(2000, 2010,3):
    if year%4 == 0 or year%400 == 0: print(year,"is a leaf year")
    else: print(year, "not a leaf year")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break
    if number%2 == 0:
        print(number)

for number in numbers:
    if number == 237:
        break
    if number%2 == 1:
        continue
    print(number)


x = []
for number in range(100, 150):
    if number%7 == 0 and  number%5 != 0:
        x.append(number)
print(x)


from datetime import datetime

print(datetime.now())

a = []
a.append(input("First name: "))
a.append(input("last name: "))
for x in a:
    print(x, end = "")

def abc(x,y):
              #b.append(input("your last name:"))
    #for y in b:
    print(" my name is %s %s and %d old" %(x,y,20))
abc("k","gk")

Add a function named list_benefits() that returns the following list of strings: "More organized code",
"More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

Add a function named build_sentence(info) which receives a single argument containing a string
and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"



a = " try   hard "
print(a.replace("  ",""))
y = a.strip()
print(y.replace("  ",""))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {1} items for ${2} adn no{0}"
print(myorder.format(quantity, itemno, price))

a = "the functions work together!"
print(a.isalpha())

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits.count("apple"))
print(len(fruits))

# Program to show various ways to read and
# write data in a file.
file1 = open("input.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
 
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes
 
file1 = open("input.txt","r+")
 
print("Output of Read function is ")
print(file1.read())
print()


x = open("input.txt", "r+")
x.write("hello")
x.close()
y = open("input.txt","r+")
print(y.read())


with open("input.txt", "r+") as f:
    #f.write("45")
#x.close()
   # y = open("input.txt","r+")
    print(f.readlines()[1])   





# Python program to
# demonstrate readline()

L = ["Geeks\n", "for\n", "Geeks\n"]

# Writing to a file
file1 = open('myfile.txt', 'w')
file1.writelines((L))
file1.close()

# Using readline()
file1 = open('input.txt', 'r')
count = 0

while True:
	count += 1

	# Get next line from file
	line = file1.readline()

	# if line is empty
	# end of file is reached
	if not line:
		break
	#print("Line{}: {}".format(count, line.strip()))
	print(f"{line.strip()}")
file1.close()
'''


def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
input = open('input.txt', 'r')
line = input.readlines()
a = int(line[0])
b = int(line[1])
c = f"plus of {a} and {b} is", str(plus(a,b))
d = f"subtraction of {a} and {b} is", str(minus(a,b))
output = (c,d)
result = open('output.txt','w')
result.write(c)
result.close()
plus(a,b)





    



















