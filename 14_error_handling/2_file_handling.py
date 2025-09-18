# it is the basic syntax of file handling try-except-finally

file=open('youtube.txt','w')
try:
    file.write('shree ganeshay namah')
finally:
    file.close()   #required to close file

# m-2 

with open('youtube2.py','w') as file:
    file.write('jsk  --  jsr')