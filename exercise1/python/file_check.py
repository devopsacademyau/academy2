import os

secret_filename = "./secrets.txt"

print('----Checking if File exists----')
listdir = os.listdir('exercise1')
listdir_system = os.popen("find .").read()
git_log = os.popen(f"git log -p -- {secret_filename}").read()

if secret_filename in listdir_system:
    raise Exception("File exists! Check your github repository!")

print(git_log)
print(listdir_system)
print('File does not exist! Well done!')


