def make_level_list(cefr):
    dic = []
    with open(cefr) as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split(',')
            if line[2] in ['A1', 'A2', 'B1']:
                dic.append(line[0])
    return dic

def search_dict(multi_word, easy_dic):
    initial = multi_word[0].lower()
    dic_name = '../data/syn_data/syn_data_{}.txt'.format(initial)
    candidate = []
    with open(dic_name, 'r') as f:
        line = f.readline()
        while line:
            line = line.split('\t')
            if line[0] == multi_word:
                while line[0] == multi_word:
                    word2 = line[4]
                    #単語のみを追加。複合語は除外。
                    if ' ' not in word2 and word2 not in candidate:
                        if word2 in easy_dic:
                            candidate.append(word2)
                    line = f.readline()
                    line = line.split('\t')
                break
            line = f.readline()
    return candidate


def write_data(multiword, lemma, easy_dic):
    candidate = search_dict(multiword, easy_dic)
    for i in range(len(candidate)):
        if multiword not in lemma:
            print('error')
        write_sebt = lemma.replace(multiword, candidate[i])
        out.write(write_sebt)

def pre_main(text_name):
    cefr = '../data/CEFR_level_list.csv'
    easy_dic = make_level_list(cefr)

    with open(text_name, 'r', encoding='utf-8', errors='ignore') as in_put:
        line = in_put.readline()
        while line:

            line2 = in_put.readline()
            line3 = in_put.readline()
            line4 = in_put.readline()
            line5 = in_put.readline()

            lemma = line2
            multiword = line5.replace('\n', '')

            write_data(multiword, lemma, easy_dic)
            while line != '\n':
                line = in_put.readline()
            line = in_put.readline()


if __name__ == '__main__':
    data_name = '../evaluation/used_data_parse/check_annotate_data_checked_parse.txt'
    out_data = 'checked(lemma).txt'

    with open(out_data, 'w') as out:
        pre_main(data_name)