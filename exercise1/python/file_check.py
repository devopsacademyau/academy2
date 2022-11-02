import os
import subprocess


print('----Checking if File exists----')
listdir = os.listdir('exercise1')
listdir_system = subprocess.check_output("find .")
git_log = subprocess.check_output("git log -p --git_history_check.py")

if 'secrets.txt' in listdir:
    raise Exception("File exists! Check your github repository!")

print(git_log)
print(listdir_system)
print('File does not exist! Well done!')


