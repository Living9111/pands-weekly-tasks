def fibonacci(number):
 return []

return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'
Traceback (most recent call last):
 File ".\myfunctions.py", line 27, in <module>
 assert fibonacci(7) == return7, 'incorrect return value for 7
try:
 fibonacci(-1)
except ValueError:
 pass
else:
 assert False, 'fibonacci missing ValueError'
 
if __name__ == '__main__':
 print("all good")
