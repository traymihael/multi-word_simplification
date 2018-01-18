with open('idiom.csv') as f:
    with open('idiom1.csv') as g1:
        lines = g1.readline()
        while lines:
            f.writeline(lines)
            lines = f.readline()
print(lines)