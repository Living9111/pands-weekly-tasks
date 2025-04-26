#a)
FILENAME = r"C:\Users\MyPC\Desktop\week 1\week 2\count.txt"
def readNumber():
 with open(FILENAME) as f:
     number = int(f.read())
 return number
num = readNumber()
print ('count text file contains:',num)

#b)
#FILENAME = "C:\Users\MyPC\Desktop\week 1\week 2\count.txt"
def writeNumber(number):
 with open(FILENAME, "wt") as f:
  f.write(str(number))
# test it
writeNumber(3)

#c)
FILENAME = r"C:\Users\MyPC\Desktop\week 1\week 2\count.txt"
def readNumber():
 with open(FILENAME) as f:
  number = int(f.read())
 return number
def writeNumber(number):
 with open(FILENAME, "wt") as f:
  f.write(str(number))
 num = readNumber()
 num += 1
 print (f"we have run this program {num} times")
writeNumber(num)

#d)
