with open("main.py", "r") as file:
    data = file.readlines()

data[57] = 'mainServerAddr = ("' + sys.argv + ')'

with open("main.py", "r") as file:
    file.writelines(data)
