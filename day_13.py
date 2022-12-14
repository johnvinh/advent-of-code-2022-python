with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

for i in range(0, len(lines), 3):
    item_1 = eval(lines[i])
    item_2 = eval(lines[i + 1])