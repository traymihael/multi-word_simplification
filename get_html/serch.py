import re
import pprint
import pandas
dic = {}
with open('idiom.csv') as f:
    line = f.readline().split('*')
    while line:
        print(line)
        dic.update({line[0] : line[1]})
        line = f.readline().split('*')
        if len(line) != 2:
            break
pprint.pprint(dic)

idiom = input()
print(dic[idiom])