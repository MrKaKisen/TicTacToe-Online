with open("main.py", "r") as file:
    data = file.readlines()

f = open("temp.temp")
mainServerAddr = f.read()
f.close()

os.remove("temp.temp")

data[57] = 'mainServerAddr = ("' + mainServerAddr + ')'

with open("main.py", "r") as file:
    file.writelines(data)
