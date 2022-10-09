import shutil
import os.path

count_lines = {}
for line in open(r'q4_urls.txt', encoding="utf8"):
    clean_line = line.rstrip()
    if clean_line not in count_lines:
        count_lines[clean_line] = 0
    count_lines[clean_line] += 1

out = open(r'new.txt', 'w')
for line in open(r'q4_urls.txt'):
    count = count_lines[line.rstrip()]
    out.write(f"{line} | {count}")

out.close()
