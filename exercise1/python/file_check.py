import os

print('----Checking if File exists----')
listdir = os.listdir('exercise1')

if 'secrets.txt' in listdir:
    raise Exception("File exists! Check your github repository!")

print('File does not exist! Well done!')


