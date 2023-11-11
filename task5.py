path = "mbox-short.txt"
file = open(path, "r")

str = ""

for line in file:
    str += line.upper()
print(str)
file.close()