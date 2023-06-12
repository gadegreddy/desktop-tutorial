
#create functions

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

#read the file
filer = open('input.txt', 'r')
line = filer.readlines()
a = int(line[0])
b = int(line[1])
filer.close()

#write the file
filew = open('output.txt', 'w')

line = filew.writelines(f"addition of {a} and {b} is: {plus(a,b)}\n")
line = filew.writelines(f"subtraction of {a} and {b} is: {minus(a,b)}\n")
line = filew.writelines(f"multiplication of {a} and {b} is: {multi(a,b)}\n")
line = filew.writelines(f"division of {a} and {b} is: {div(a,b):.4f}\n")
filew.close()

#call functions
plus(a,b)
minus(a,b)
multi(a,b)
div(a,b)




































































