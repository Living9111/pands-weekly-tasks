FILENAME = r"C:\Users\MyPC\Desktop\week 1\week 2\count.txt"
def readNumber():
 with open(FILENAME) as f:
     number = int(f.read())
 return number
num = readNumber()
print ('count text file contains:',num)