6. Why does this expression cause an error? How can you fix it? 
# python can only concatenate str (not "int") to str, so we convert integer data type (ie 99) to string
message = ('I have eaten ' + str(99) + ' burritos.')
print (message)
# https://www.digitalocean.com/community/tutorials/python-concatenate-string-and-int

7. Why is eggs a valid variable name while 100 is invalid?
    
# variable names in python programming languages cannot start with a number. 
# They must begin with a letter (a-z, A-Z) or an underscore (_).  
# Eggs is valid because it starts with a letter. 100 is invalid because it starts with a number.
#  Variable names need to start with a letter or underscore. "100" starts with a number, violating this rule.


 8. What three functions can be used to get the integer, floating-point number, or
string version of a value?

# int() - converts a value to an integer
# float() - converts a value to a floating-point number
# str() - converts a value to a string