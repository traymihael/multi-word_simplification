#辞書作成[[単語、難易度（数字）] ... ]
def make_level_list(cefr):
    dic = []
    level = {'A1':1,'A2':2,'B1':3,'B2':4,'C1':5,'C2':6}
    with open(cefr) as f:
        line = f.readline()
        while len(line) > 3:
            line = line.split(',')
            dic.append([line[0], level[line[2].replace('\n', '')]])
            line = f.readline()

    return dic

def cefr_check(candidate, cefr_dic):
    candidate2 = []
    for word in candidate:
        flg = 0
        for i in range(len(cefr_dic)):
            if cefr_dic[i][0] == word and cefr_dic[i][1] <= 3:
                flg = 1
                break
        if flg and word not in candidate2:
            candidate2.append(word)
    return candidate2

def search_dict(multi_word, cefr_dic):

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
                    if ' ' not in word2:
                        candidate.append(word2)
                    line = f.readline()
                    line = line.split('\t')
                break
            line = f.readline()
        candidate2 = cefr_check(candidate, cefr_dic)
        return candidate2


if __name__ == '__main__':
    input_data = 'more_B2_2.txt'
    output_data = 'annotate_data.txt'
    cefr = '../data/CEFR_level_list.csv'
    cefr_dic = make_level_list(cefr)

    with open(input_data, 'r') as f, open(output_data, 'w') as out:

        line1 = f.readline()
        while line1:
            out.write(line1)
            line2 = f.readline()
            while line2 != '\n':
                out.write(line2)
                line2_kari = line2.split('\t')
                multi_word = line2_kari[2]
                candidate = search_dict(multi_word, cefr_dic)
                for word in candidate:
                    out.write('\t\t'+word+'\n')
                line2 = f.readline()

            line1 = f.readline()