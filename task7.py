file_input = open("feedback.txt", "r")

positive = ""
positive_count = 0

negative = ""
negative_count = 0

for line in file_input:
    if "Positive:" in line:
        positive += line
        positive_count += 1
        continue

    negative += line
    negative_count += 1

file_input.close()

file = open("positive.txt", "w")
file.write(positive)
file.close()

file = open("negative.txt", "w")
file.write(negative)
file.close()

file = open("feedback_analysis.txt", "w")
file.write(f"""Total feedbacks: {positive_count + negative_count}, count of positive feedbacks: {positive_count}, count of negative feedbacks: {negative_count}""")
file.close()