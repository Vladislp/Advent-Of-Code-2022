# For help on this day, big thanks to: https://galaxyinferno.com/how-to-solve-advent-of-code-2022-day-3-with-python/

with open('input.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]

# Part 1

rucksack_sum = 0
for rucksack in rucksacks:
    # split in half 
    first_half = set(rucksack[:len(rucksack)//2])
    second_half = set(rucksack[len(rucksack)//2:])
    # get overlap through set logic (intersection of two sets)
    overlap_char = (first_half.intersection(second_half)).pop()

    # translate to ascii and substract the base ('A' is 65, 'B' is 66 and so on) and add the new base
    if overlap_char.isupper():
        rucksack_sum += ord(overlap_char) - ord('A') + 27
    else:
        rucksack_sum += ord(overlap_char) - ord('a') + 1
rucksack_sum

# Part 2

#rucksack_sum = 0
#while len(rucksacks) > 0:
    # take out first 3 entries
#    first_rucksack = set(rucksacks.pop())
#    second_rucksack = set(rucksacks.pop())
#    third_rucksack = set(rucksacks.pop())
#    # get overlap through set logic (intersection of two sets applied twice)
#    overlap_char = ((first_rucksack.intersection(second_rucksack)).intersection(third_rucksack)).pop()

    # translate to ascii and substract the base ('A' is 65, 'B' is 66 and so on) and add the new base
#    if overlap_char.isupper():
#        rucksack_sum += ord(overlap_char) - ord('A') + 27
#    else:
#        rucksack_sum += ord(overlap_char) - ord('a') + 1
#rucksack_sum