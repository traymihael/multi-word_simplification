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

def make_dictionary_evp():
    dic = []
    name = '../data/EVP/English_Vocabulary_Profile(EVP)AmE_multi.txt'

    with open(name) as g:
        line = g.readline()
        while line:
            line = line.replace('\n', '')
            line = line.split('\t')
            words = line[1]
            rank = line[4]
            dic.append([words,rank])
            line = g.readline()
    return dic

def search_overlap(file1, file2):
    with open(file1, 'r') as f, open(file2, 'r') as g:
        data = []
        overlap_data = []
        for line in f:
            line = line.split('\t')
            data.append(line[0])
        for line in g:
            line = line.replace('\n', '')
            line = line.split('\t')
            if line[0] in data:
                overlap_data.append([line[0], line[1]])
    return overlap_data

def search_cefr_level(overlap_data, dic_cefr):
    for i in range(len(overlap_data)):
        for j in range(len(dic_cefr)):
            if overlap_data[i][0] == dic_cefr[j][0]:
                overlap_data[i].append(dic_cefr[j][1])
                break

def search_evp_level(overlap_data, dic_evp):
    for i in range(len(overlap_data)):
        for j in range(len(dic_evp)):
            if overlap_data[i][0] == dic_evp[j][0]:
                overlap_data[i].append(dic_evp[j][1])
                break

def write_data(out_name, overlap_data):
    with open(out_name, 'w') as out:
        for line in overlap_data:
            out.write('{}\n'.format('\t'.join(line)))

if __name__ == '__main__':
    file1 = '../data/Rice_University/count_evp.txt'
    file2 = '../data/Rice_University/count_cefr.txt'
    dic_cefr = make_dictionary_cefr()
    dic_evp = make_dictionary_evp()

    overlap_data = search_overlap(file1, file2)
    search_cefr_level(overlap_data, dic_cefr)
    search_evp_level(overlap_data, dic_evp)

    out_name = '../data/Rice_University/overlap_data.txt'
    #print(overlap_data[10])
    write_data(out_name, overlap_data)