import os
from collections import defaultdict

def count_number(files, count_multi, number, dic):
    # for file in files:
    #     # input_name = '../data/corpus4/count{}/{}'.format(number, file)
    #     # input_name = '../data/Rice_University/{}/{}_count/{}/{}'.format(number, number, dic, file)
    #     input_name = file
    #     #print(input_name)
    #     with open(input_name, 'r') as f:
    #         for line in f:
    #             line = line.replace('\n', '')
    #             line = line.split('\t')
    #             # a = int(line[1])
    #             # count_multi[line[0]] += int((a+1)/2)
    #             count_multi[line[0]] += int(line[1])

    for file in files:
        input_name = '../data/corpus4/count{}{}/{}'.format(number, evp, file)
        #print(input_name)
        with open(input_name, 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                line = line.split('\t')
                a = int(line[1])
                # count_multi[line[0]] += int((a+1)/2)
                count_multi[line[0]] += int(line[1])


def write_data(count_multi, output_name):
    count_multi = sorted(count_multi.items(), key=lambda x: x[1], reverse=True)
    with open(output_name, 'w') as out_put:
        for i in range(len(count_multi)):
            out_put.write(count_multi[i][0] + '\t' + str(count_multi[i][1]) + '\n')



if __name__ == '__main__':
    # text_name = ['economics', 'psychology', 'sociology']
    # dictionary = ['cefr', 'evp']
    # for dic in dictionary:
    #     count_multi = defaultdict(int)
    #     for number in text_name:
    #         files = ['../data/Rice_University/{}/{}_count/count_{}.txt'.format(number, number, dic)]
    #         count_number(files, count_multi, number, dic)
    #     output_name = '../data/Rice_University/count_{}.txt'.format(dic)
    #     write_data(count_multi, output_name)
    dic = 1
    number = 2
    evp = ''
    output_name = '../data/corpus4/count{}{}/count{}.txt'.format(number, evp, number)
    files = os.listdir('../data/corpus4/count{}{}'.format(number, evp))
    count_multi = defaultdict(int)
    count_number(files, count_multi, number, dic)
    #print(output_name, len(count_multi))
    write_data(count_multi, output_name)
