import pos_exchange as pos_ex

def make_dictionary_CEFR():
    dic = []
    name = '../data/CEFR_level_list.csv'
    with open(name) as h:
        line = h.readline()
        while line:
            line = line.replace('\n', '')
            words = line.split(',')
            dic.append(words)
            line = h.readline()
    return dic

def check(words, pos, dic):
    level = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 4, 'C1': 5, 'C2': 6}
    rank = {1: 'A1', 2: 'A2', 3: 'B1', 4: 'B2', 5: 'C1', 6: 'C2', 7: 'unknown'}
    word_rank = 0

    for i in range(len(words)):
        flg, flg2 = 0, 0
        word_rank_kari = 0
        if pos_ex.pos_exchange_cefr(words[i], pos[i]) == 'preposition':
            if word_rank < 1:
                word_rank = 1
            continue
        for j in range(len(dic)):
            if words[i] == dic[j][0]:
                if pos_ex.pos_exchange_cefr(words[i], pos[i]) == dic[j][1]:
                    if word_rank < level[dic[j][2]]:
                        word_rank = level[dic[j][2]]
                    flg = 1
                    flg2 = 0
                    break
                else:
                    if word_rank < level[dic[j][2]]:
                        word_rank_kari = level[dic[j][2]]
                    flg2 = 1
                    flg = 1
        if flg2 == 1:
            if word_rank_kari > word_rank:
                word_rank = word_rank_kari

        if flg == 0:
            word_rank = 7
            break

    return rank[word_rank]


if __name__ == '__main__':
    dic = make_dictionary_CEFR()
    for i in range(26):
        name = '../make_dict/dic_simple/dic_{}.txt'.format(chr(i + 97))
        #name = '../make_dict/dic_simple/sample.txt'
        name2 = 'simple_level2/dic_{}.txt'.format(chr(i + 97))
        print(name)
        with open(name2, 'w') as f, open(name, 'r') as g:
                line = g.readline()
                while line:
                    line = line.replace('\n', '')
                    line = line.split('\t')
                    words = line[0].split()
                    pos = line[1].split()
                    word_rank = check(words, pos, dic)
                    f.write('\t'.join(line) + '\t' + word_rank + '\n')
                    line = g.readline()
