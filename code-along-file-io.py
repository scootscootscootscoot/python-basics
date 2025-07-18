
'''
file_path = 'data.csv'

print(file_path)

file = open(file_path, 'r')
file = open(file_path, 'w')
file = open(file_path, 'a')
file = open(file_path, 'r+')'''

## write function will write a new file or overwrite an existing one 
'''
file = open("example.txt", "w")
file.write("Hello,world!\n")
file.write("This is line 2\n")
file.close()'''

## open a file using the 'with' statement
'''
with open("example-with.txt", "w") as file:
    file.write("we wrote this using the with keyword!\n")'''


# read function to read contents of a file
'''
with open("exmple-with.txt", "r") as file:
    contents = file.read()
    print(contents)   '''

# use for loop to read lines from a file
'''
with open("example-with.txt", "r")as file:
    for line in file:
        print(line.strip())
        '''


# append to file

with open("example-with.txt", "a") as file:
          file.write("this is an appended line!\n")