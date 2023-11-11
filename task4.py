path = "mbox-short.txt"
file = open(path, "r")

i = 1
max_w = ""
for line in file:
    print(f"Symbol count in line {i}: {len(line) - 1}")
    i+=1

    words = line.split(" ")
    
    for word in words:
        if len(word) > len(max_w): max_w = word

file.close()

print(f"Longest word is {max_w}")