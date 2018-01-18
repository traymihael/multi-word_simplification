#辞書作成[[単語、難易度（数字）] ... ]
def make_level_list(cefr):
    dic = []
    #level = {'A1':1,'A2':2,'B1':3,'B2':4,'C1':5,'C2':6}
    with open(cefr) as f:
        line = f.readline()
        while len(line) > 3:
            line = line.split(',')
            dic.append([line[0], line[2].replace('\n', '')])
            line = f.readline()

    return dic

def pre_proc(out):
    out.write("<style type='text/css'>\n")
    out.write(".table0 th {\n\tbackground-color: #cccccc;\n\twidth: 90px;\n}\n")
    out.write(".table1 {\n\tborder-collapse: collapse;\n}\n")
    out.write(".table1 th {\n\tbackground-color: #cccccc;\n\twidth: 90px;\n}</style>\n")

def write_text(line, index, out):
    words = line.split()
    for i in index:
        words[int(i)] = '<b>{}</b>'.format(words[int(i)])
    sentence = ' '.join(words)
    out.write("<br>{}<br><br>\n\n".format(sentence))

def search_word_level(word, dic_cefr):
    word_level = []
    for i in range(len(dic_cefr)):
        if dic_cefr[i][0] == word:
            while dic_cefr[i][0] == word:
                word_level.append(dic_cefr[i][1])
                i += 1
            break
    return word_level

def write_out(line1, multi_word, candidate, out, count, index, level, dic_cefr):
    out.write("<HR>\n<b>input text</b>:\n")
    write_text(line1, index, out)
    out.write("<br><b>target list</b>:<br>\n<table class='table0' border=1>\n")
    # out.write("<tr><th>ID</th><th>index</th><th>target</th><th>pos</th><th>difficulty</th><th>head</th><th>head_pos</th><th>head_score</th></tr>\n")
    # out.write("<tr bgcolor='powderblue'><td>{}</td><td>{}</td><td>{}</td><td></td><td>{}</td><td></td><td></td><td></td></tr>\n".format(count, ','.join(index), multi_word, level))
    out.write("<tr><th>ID</th><th>index</th><th>target</th><th>difficulty</th><th>C.S</th></tr>\n")
    out.write("<tr bgcolor='powderblue'><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td></td></tr>\n".format(count, ','.join(index), multi_word, level))
    out.write("</table><br>\n<br><b>candidate list</b> : <b>key</b>={}\n".format(multi_word))
    # out.write("<table class='table1' border=1><tr><th>candidate</th><th>difficulty</th><th>score(log_probability)</th><th>judge</th></tr>\n")
    out.write("<table class='table1' border=1><tr><th>candidate</th><th>difficulty</th><th>judge</th></tr>\n")
    for word in candidate:
        word_level = search_word_level(word, dic_cefr)
        out.write("<tr bgcolor='powderblue'><td>{}</td><td>{}</td><td></td></tr>\n".format(word, ','.join(word_level)))
    out.write("</table><br>")

def make_htmltext(text_name, out_name, dic_cefr):
    with open(text_name, 'r') as text, open(out_name, 'w') as out:
        pre_proc(out)
        line1 = text.readline()
        count = 0
        while line1:
            line1 = line1.replace('\n', '')
            line2 = text.readline()
            while line2 != '\n':
                # count += 1
                line2 = line2.replace('\n', '')
                line2 = line2.split('\t')
                multi_word = line2[2]
                index = line2[5].replace('\n', '')
                index = index.split(',')
                # index = ['0', '1']
                level = line2[4]
                candidate = []
                line3 = text.readline()
                while '\t\t' in line3:
                    line3 = line3.split('\t')
                    word = line3[2].replace('\n', '')
                    candidate.append(word)
                    line3 = text.readline()
                if level in ['B2', 'C1', 'C2'] and 'c:' in line2:
                    count += 1
                    write_out(line1, multi_word, candidate, out, count, index, level, dic_cefr)
                line2 = line3


            line1 = text.readline()
    print(count)


if __name__ == '__main__':
    number = '1'

    text_name = 'annotate_data{}.txt'.format(number)
    out_name = 'html_file/annotate{}.html'.format(number)
    cefr = '../data/CEFR_level_list.csv'
    dic_cefr = make_level_list(cefr)
    make_htmltext(text_name, out_name, dic_cefr)