import os

print('----Checking if File exists----')
listdir = os.listdir('exercise1')
listdir_system = os.system("find .")
git_log = os.system("git log -p -- './secrets.txt'")

if 'secrets.txt' in listdir:
    raise Exception("File exists! Check your github repository!")

print(git_log)
print(listdir_system)
print('File does not exist! Well done!')


