path = "poetry.txt"
file = open(path, "r")

l_count_not_for_T = 0
l_count_not_for_d = 0
w_count_is_upper = 0
for line in file:
    if line[0] != "T": l_count_not_for_T += 1
    if line[-1] == "d" : l_count_not_for_d += 1
    words = line.split(" ")
    for word in words:
        if word[0].isupper(): w_count_is_upper +=1


file.close()
print(f"""
      Strings that do not begin with the letter 'T': {l_count_not_for_T},
      Strings that do not end with the letter 'd': {l_count_not_for_d},
      Words that start with a capital letter: {w_count_is_upper}.""")