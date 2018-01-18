with open('proverb.txt', 'r') as f, open('proverb_clean.txt', 'w') as g:
    line = f.readline().split('*')
    while line:
        line2 = line[0].replace('.', '')
        line3 = line2 + '*' + line[1]
        g.write(line3)
        line = f.readline().split('*')
        if len(line) != 2:
            break


