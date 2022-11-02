import os

print('----Checking if File exists----')
listdir = os.listdir('exercise1')
listdir_system = os.system("find .")

if 'secrets.txt' in listdir:
    raise Exception("File exists! Check your github repository!")

print(listdir_system)
print('File does not exist! Well done!')


