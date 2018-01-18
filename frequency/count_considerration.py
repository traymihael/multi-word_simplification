def make_dictionary_cefr():
    dic = []
    for i in range(26):
        #name = '../make_dict/dic_simple/dic_{}.txt'.format(chr(i+97))
        name = '../make_dict/simple_level2/dic_{}.txt'.format(chr(i + 97))
        #name = 'simple.txt'
        with open(name) as g:
            line = g.readline()
            while line:
                #dic_kari = []
                line = line.replace('\n', '')
                line = line.split('\t')
                words = line[0]
                rank = line[4]
                dic.append([words,rank])
                line = g.readline()
    return dic

def write_data(rank, line):
    if rank == 'A1':
        A1.write(line)
    if rank == 'A2':
        A2.write(line)
    if rank == 'B1':
        B1.write(line)
    if rank == 'B2':
        B2.write(line)
    if rank == 'C1':
        C1.write(line)
    if rank == 'C2':
        C2.write(line)
    if rank == 'unknown':
        unknown.write(line)

def check(text_name, dic):
    with open(text_name, 'r') as f:
        for line in f:
            line2 = line.split('\t')
            for i in range(len(dic)):
                if line2[0] == dic[i][0]:
                    rank = dic[i][1]
                    break
            write_data(rank, line)


if __name__ == '__main__':
    text_name = '../data/corpus4/count.txt'
    level = ['A1','A2','B1','B2','C1','C2','unknown']
    data_save_name = []
    dic = make_dictionary_cefr()
    for i in level:
        data_save_name.append('../data/corpus4/count_{}.txt'.format(i))

    with open(data_save_name[0], 'w') as A1,open(data_save_name[1], 'w') as A2,open(data_save_name[2], 'w') as B1,open(data_save_name[3], 'w') as B2,open(data_save_name[4], 'w') as C1,open(data_save_name[5], 'w') as C2,open(data_save_name[6], 'w') as unknown:
        check(text_name, dic)