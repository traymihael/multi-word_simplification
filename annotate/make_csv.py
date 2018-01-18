import make_html

def make_csvlist(text, dic_cefr, version):
    #text_name = '../text_matching/data4/{}.txt'.format(text)
    save_name = 'csv_file/check_annotate_data{}.txt'.format(version)
    with open(text, 'r') as text, open(save_name, 'w') as out:
        out.write('TargetID\tIndex\tInputText\tTarget\tcandidate\tCEFR\tC.S.\tjudge\tcomment\n')

        line1 = text.readline()
        count = 0
        while line1:
            line1 = line1.replace('\n', '')
            line2 = text.readline()
            while line2 != '\n':
                line2 = line2.split('\t')
                multi_word = line2[2]
                index = line2[5].replace('\n', '')
                index = index.split(',')
                multi_difficulty = line2[4]

                level = []
                CorD = line2[1].replace(':', '')
                candidate = []
                line3 = text.readline()
                while '\t\t' in line3:
                    line3 = line3.split('\t')
                    word = line3[2].replace('\n', '')
                    candidate.append(word)
                    line3 = text.readline()
                    level.append(make_html.search_word_level(word, dic_cefr))
                #write_out(line1, multi_word, candidate, out, count, index, level)

                # 連続かのチェック
                flg = 1
                for i in range(len(index)-1):
                    if int(index[i+1]) - int(index[i]) != 1:
                        flg = 0
                        break

                if multi_difficulty in ['B2', 'C1', 'C2'] and flg == 1:
                    count += 1
                    write(line1, multi_word, candidate, out, count, level, CorD, index)
                line2 = line3

            line1 = text.readline()

def write(line1, multi_word, candidate, out, count, level,CorD, index):
    #out.write('{}\t{}\t{}\t{}\n'.format(count, ','.join(index), line1, multi_word))
    for i in range(len(candidate)):
        out.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(count, ','.join(index), line1, multi_word, candidate[i], ','.join(level[i])))



if __name__ == '__main__':
    version = '1'

    text = 'annotate_data{}.txt'.format(version)
    cefr = '../data/CEFR_level_list.csv'
    dic_cefr = make_html.make_level_list(cefr)
    make_csvlist(text, dic_cefr, version)