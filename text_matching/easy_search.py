def make_dic():
    dic = []
    with open('low_high.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            dic.append(line)
    return dic

def search_diff(text_name):
    easy = ['A1', 'A2', 'B1']
    with open(text_name, 'r') as f:
        for line in f:
            flg = 0
            for a in easy:
                if a in line:
                    flg = 1
            if flg == 0:
                continue

            line = line.split('\t')
            words = line[2]
            for i in range(len(dic)):
                if dic[i] == words:
                    out_put.write(words+'\n')
                    print(words)
                    break


if __name__ == '__main__':
    dic = make_dic()

    out_put_name = 'out_put.txt'
    with open(out_put_name, 'w') as out_put:
        for i in range(12):
            text_name = 'data4/out_L{}.txt'.format(i+1)
            search_diff(text_name)