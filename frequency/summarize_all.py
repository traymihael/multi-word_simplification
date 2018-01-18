import os
import glob
from collections import defaultdict

def count_number(input_name, count_multi):
    with open(input_name, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split('\t')
            #a = int(line[1])
            count_multi[line[0]] += int(line[1])

def write_data(count_multi, output_name):
    count_multi = sorted(count_multi.items(), key=lambda x: x[1], reverse=True)
    with open(output_name, 'w') as out_put:
        for i in range(len(count_multi)):
            out_put.write(count_multi[i][0] + '\t' + str(count_multi[i][1]) + '\n')

def process_cefr(count_multi):
    for i in range(26):
        name = '../make_dict/simple_level2/dic_{}.txt'.format(chr(i + 97))
        with open(name) as g:
            for line in g:
                line = line.split('\t')
                words = line[0]
                count_multi[words] += 0

def process_evp(count_multi):
    name = '../data/EVP/English_Vocabulary_Profile(EVP)AmE_multi.txt'
    with open(name) as g:
        for line in g:
            line = line.replace('\n', '')
            line = line.split('\t')
            words = line[1]
            count_multi[words] += 0

if __name__ == '__main__':
    count_multi = defaultdict(int)
    evp = ''
    output_name = '../data/corpus4/count.txt'
    for i in range(6):
        input_name = '../data/corpus4/count{}{}/count{}.txt'.format(i, evp, i)
        count_number(input_name, count_multi)
    if evp == 'evp':
        process_evp(count_multi)
    else:
        process_cefr(count_multi)

    write_data(count_multi, output_name)

