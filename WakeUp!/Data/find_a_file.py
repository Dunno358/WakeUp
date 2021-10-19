import os

disks="ABEFGHIJKLMNOPRSTUWYZDC"

def findFile(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

lookFor = input("Enter name of file you want to find(with extension)\n: ")

print("\nSearching throught your drives and folders...\nThis may take a while...\n")
for x in disks:
    check = findFile(lookFor,r"{}:\\".format(x))
    if check != None:
        print("Path located! Here it is:\n",check,"\n")
        break
os.system("pause")
