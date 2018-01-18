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

def check(input_data, count, cefr_dic, pre_multi):

    with open(input_data, 'r') as f:
        line1 = f.readline()
        while line1:
            flg = 1
            line2 = f.readline()

            while line2 != '\n':
                line2_kari = line2.split('\t')
                multi_word = line2_kari[2]

                if multi_word in pre_multi:
                    line2 = f.readline()
                    continue

                pre_multi.append(multi_word)
                candidate = search_dict(multi_word, cefr_dic)

                if len(candidate) >= 1:
                    if flg:
                        out.write(line1)
                        flg = 0

                    out.write(line2)
                    for word in candidate:
                        out.write('\t\t' + word + '\n')
                    count += 1

                if count % 10 == 0:
                    print(count)
                line2 = f.readline()

            line1 = f.readline()
            if flg == 0:
                out.write('\n')

def process():
    input_name = 'used_multi_list.txt'
    pre_multi = []
    with open(input_name, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            pre_multi.append(line)
    return pre_multi

if __name__ == '__main__':

    cefr = '../data/CEFR_level_list.csv'
    cefr_dic = make_level_list(cefr)
    pre_multi = process()
    count = 0
    # output_data = 'annotate_data_test.txt'
    # with open(output_data, 'w') as out:
    #     text_name = '../text_matching/out_put.txt'
    #     print(text_name)
    #     check(text_name, count, cefr_dic, pre_multi)


    text_candidate = ['economics', 'psychology', 'sociology']
    output_data = 'annotate_data.txt'
    with open(output_data, 'w') as out:
        for i in text_candidate:
            text_name = '../text_matching/Rice_text/1/{}.txt'.format(i)
            print(text_name)
            check(text_name, count, cefr_dic, pre_multi)