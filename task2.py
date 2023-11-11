path = "output2.txt"
file = open(path, "w")

while(True):
    str = input()
    if not str: break
    file.write(str + "\n")
file.close()


# reading
content = open(path, "r")
line_count = 0
symbol_count = 0
for line in content:
    line_count += 1
    symbol_count += len(line) - 1 # 1 symbol is for "\n"

content.close()
print(f"Lines: {line_count}, Symbols: {symbol_count}")