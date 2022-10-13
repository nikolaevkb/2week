count_lines = {}
for line in open(r'q41.txt'):
    clean_line = line.rstrip()
    if clean_line not in count_lines:
        count_lines[clean_line] = 0
    count_lines[clean_line] += 1

out = open(r'new.txt', "w")
for line in open(r'q41.txt'):
    count = count_lines[line.rstrip()]
    out.write(f"{line} ! {count}")

out.close()