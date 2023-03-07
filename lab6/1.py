import os
path = input()
#path = '/Users/nazerkeabubakirovna/PycharmProjects/Project'
for name in os.listdir(path):
        print(name)