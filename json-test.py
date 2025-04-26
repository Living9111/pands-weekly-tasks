import json
FILENAME =r"C:\Users\MyPC\Desktop\week 1\week 2\testdict.json"
def readDict():
 with open(FILENAME) as f:
   return json.load(f)
somedict = readDict()
print(somedict)