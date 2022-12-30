with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

total_code = 0
total_in_memory = 0
for line in lines:
    eval_line = eval(line)
    total_code += len(line)
    total_in_memory += len(eval_line)
print(total_code - total_in_memory)