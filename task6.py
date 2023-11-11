path = "mbox-short.txt"
file = open(path, "r")

result = 0
for line in file:
    count = line.count("@")
    if count:
        print(line)
        result += count
file.close()
print(f"count of @: {result}")