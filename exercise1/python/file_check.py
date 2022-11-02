import os

secret_filename = "./secrets.txt"

print('----Checking if File exists----')
listdir = os.listdir('exercise1')
listdir_system = os.system("find .")
git_log = os.system(f"git log -p -- {secret_filename}")

if secret_filename in listdir:
    raise Exception("File exists! Check your github repository!")

print(git_log)
print(listdir_system)
print('File does not exist! Well done!')


