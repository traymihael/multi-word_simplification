import os

if __name__ == '__main__':
    files = os.listdir('csv_file')
    word_list = []
    pre_word = ''
    for file in files:
        text_name = 'csv_file/{}'.format(file)
        with open(text_name, 'r') as f:
            for line in f:
                line = line.split('\t')
                try:
                    multiword = line[3]
                except:
                    continue
                if multiword == 'Target':
                    continue
                if multiword == pre_word:
                    continue
                word_list.append(multiword)
                pre_word = multiword

    out_name = 'used_multi_list.txt'
    with open(out_name, 'w') as g:
        for line in word_list:
            g.write('{}\n'.format(line))