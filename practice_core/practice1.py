from pprint import pprint

with open('text.txt') as f:
    line = f.readline()
    lines = line.strip().split('.')
    pprint(lines)
with open('text2.txt', 'w') as g:
    for i in range(len(lines)):
        g.write('.'.join([lines[i].strip(), '\n']))