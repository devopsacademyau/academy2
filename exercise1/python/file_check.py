import os

secret_filename = "./exercise1/secrets.txt"

print('----Checking if File exists----')
listdir = os.listdir('exercise1')
listdir_system = os.popen("find .").read().split('\n')
git_log = os.popen(f"git log -p -- {secret_filename}").read()

print(listdir)

#print(git_log)
#print(listdir_system)

if secret_filename in listdir_system:
    print("File exists! Check your github repository!")
    #raise Exception("File exists! Check your github repository!")

if git_log:
    print("File exists in your Git History! Please check your github log!")


# print('File does not exist! Well done!')


