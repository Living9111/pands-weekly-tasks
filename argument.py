
# This script counts the number of occurrences of the letter 'e' in a text file.

filename = 'textfile.txt'  # Define the filename
with open('c:/Users/MyPC/Desktop/week 1/week 2/textfile.txt', 'r') as f:  # Open the file in read mode
     s = f.read()  # Read the file into a string
     count = s.count('e')  # Count the number of 'e' characters
     print(f"Count of 'e' in the text file is: {count}")



# This script counts the number of occurrences of the letter 'e' in a text file and if file doesnot exist throws error.

filename = 'textfile.txt'
try:   # Define the filename
        with open('c:/Users/MyPC/Desktop/week 1/week 2/textfile.txt', 'r') as f:  # Open the file in read mode
            s = f.read()  # Read the file into a string
            count = s.count('e')  # Count the number of 'e' characters
            print(f"Count of 'e' in the text file is: {count}")
except FileNotFoundError:
          print("File not found. Check the name of the file.")
      
      