data = []
# Open file
with open('Data.txt') as file:
    # We keep track of each entry in file
    score = 0
    # Read line in
    for line in file.readlines():
        # Remove '/n' elemendist
        line = line.strip()
        # If it an empty string
        if line == '':
            # then we append final score to the data
            data.append(score)
            # Reset "score" variable to 0
            score = 0
        else:
            # If it is not an empty string, then change it to the int and add to the score variable
            score += int(line)
# In PART 1 of this question, we are asked to find the max value of calories
print("PART 1 SOLUTION: ", max(data))
# Basicaly we sort this list
data = sorted(data)
# We could type just reverse list and take first 3 value...but this works as well
print("PART 2 SOLUTION: ", data[-1] + data[-2] + data[-3])
