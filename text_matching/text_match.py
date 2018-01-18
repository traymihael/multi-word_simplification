#import corenlp
import ngram
from pprint import pprint
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib
import xml.etree.ElementTree as ET
from graphviz import Digraph
import search_tree
import pos_exchange as pos_ex
import judge_insert
import multi_level
import pos_exchange as pos_ex
import cos_similarity
import sys
sys.path.append('../word2vec')
import search_word2vec

matplotlib.rcParams["font.family"] = 'TakaoPGOthic'

#corenlp_dir = "/home/ashihara/stanford-corenlp-full-2015-01-29/"
#parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

def ngramed(length, lemma):
    ngram_returm = []
    for i in range(len(lemma) - length + 1):
        ngram_returm.append([])
        for j in range(length):
            ngram_returm[i].append(lemma[i+j])

    return ngram_returm

def search_paraphrase(multi_word):
    initial = multi_word[0]
    dic_name = '../data/syn_data_{}.txt'.format(initial)
    previous = ''
    with open(dic_name) as l:
        line = l.readline()
        while line:
            line = line.split('\t')
            if line[0] == multi_word:
                while line[0] == multi_word:
                    if previous != line[2]:
                        out_put.write('\t{}\n'.format(line[2]))
                        previous = line[2]
                    line = l.readline()
                    line = line.split('\t')
                return

            line = l.readline()

def make_graph(co_dependence):
    G = Digraph(format='png')
    G.attr('node', shape='circle')
    dep = co_dependence.findall('dep')
    for i in dep:
        governor = i.find('governor')

        dependent = i.find('dependent')
        a = governor.text
        b = dependent.text
        G.node(governor.get('idx'), a)
        G.node(dependent.get('idx'), b)
        G.edge(governor.get('idx'),dependent.get('idx'))
    G.render(view=True)

def search_pos_level(words):
    words = ' '.join(words)
    index = words[0].lower()
    #name = '../make_dict/dic_simple/dic_{}.txt'.format(index)
    name = '../make_dict/simple_level2/dic_{}.txt'.format(index)
    with open(name) as h:
        line = h.readline()
        while line:
            line = line.replace('\n', '')
            line = line.split('\t')
            if words == line[0]:
                word_pos = [line[1], line[3]]
                level = line[4]
                break
            line = h.readline()
        pos = word_pos[0].split()
        for i in range(len(pos)):
            pos[i] = pos_ex.pos_exchange_simple(pos[i])
        word_pos[0] = ' '.join(pos)
    return word_pos, level

def write_inserted(inserted, parent_pos, candidate_num):
    out_put.write('\t\t\t({})['.format(parent_pos[candidate_num]))
    kari = []
    for j in range(len(inserted[candidate_num])):
        kari.append(','.join(inserted[candidate_num][j]))
    for j in range(len(kari)):
        out_put.write('({})'.format(kari[j]))
    out_put.write(']\n')

    '''
    for i in range(len(inserted)):
        out_put.write('\t\t\t({})['.format(parent_pos[i]))
        kari = []
        for j in range(len(inserted[i])):
            kari.append(','.join(inserted[i][j]))
        for j in range(len(kari)):
            out_put.write('({})'.format(kari[j]))
        out_put.write(']\n')
    '''
    #out_put.write('\n')

def check_word_level_cefr(words, pos, locate):
    dic = multi_level.make_dictionary_CEFR()
    pos_tag = []
    for i in locate:
        pos_tag.append(pos[i])
    pos = pos_tag
    word_rank = multi_level.check(words, pos, dic)
    return word_rank

def check_word_level_evp(multi_word):
    name = '../data/EVP/English_Vocabulary_Profile(EVP)AmE_multi.txt'
    multi_word = ' '.join(multi_word)
    with open(name) as g:
        line = g.readline()
        while line:
            if multi_word in line:
                line = line.replace('\n', '')
                line = line.split('\t')
                word_lank = line[4]
                break
            line = g.readline()
    return word_lank

def search_wordpos(locate, pos):
    word_pos = []
    for i in range(len(locate)):
        word_pos.append(pos[locate[i]])

    for i in range(len(word_pos)):
        word_pos[i] = pos_ex.pos_exchange_simple(word_pos[i])
    word_pos = ' '.join(word_pos)
    return word_pos

def check(word, lemma, pos, coreference, parse, dictionary):
    out_put.write(' '.join(word) + '\n')
    flg, flg2 = -1, 0
    count_text = 0
    easy_multi = ['A1', 'A2', 'B1']

    for i in range(len(dic)):
        for j in range(len(dic[i])):
            locate = []
            locate_coount = 0
            #同順非連続
            if len(set(dic[i][j])) == len(set(dic[i][j]) & set(lemma)):
                verif = lemma.copy()
                #print(dic[i][j])
                for k in range(len(dic[i][j])):
                    #print(dic[i][j])
                    if dic[i][j][k] not in verif:
                        break
                    index = verif.index(dic[i][j][k])
                    if k == 0:
                        locate_coount = index
                    else:
                        locate_coount = locate_coount + index + 1
                    locate.append(locate_coount)

                    for l in range(index+1):
                        verif.pop(0)
                    if k == len(dic[i][j]) - 1:
                        #print(dic[i][j])
                        candidate = dic[i][j]
                        flg = 1

            #同順連続
            if flg == 1:
                if ' '.join(dic[i][j]) in ' '.join(lemma):
                    flg = 2

            # 同順非連続
            if flg == 1:
                #print(dic[i][j])
                #word_pos, level = search_pos_level(dic[i][j])
                word_pos = search_wordpos(locate, pos)
                parent_pos, inserted, multi_index = search_tree.main_tree(word, lemma, pos, parse, dic[i][j])
                candidate_num, flg_ins = judge_insert.inserte_check(word_pos.split(), inserted)

                if dictionary == 'cefr':
                    level = check_word_level_cefr(dic[i][j], pos, locate)
                elif dictionary == 'evp':
                    level = check_word_level_evp(dic[i][j])
                #難しい複合語のみ
                # if level in easy_multi:
                #     flg_ins = 0
                if flg_ins:
                    out_put.write('\td:\t' + ' '.join(candidate)
                                  + '\t[{}]'.format(word_pos) + '\t{}\n'.format(level))
                    write_inserted(inserted, parent_pos, candidate_num)
                    #search_word2vec.main(candidate, out_put)
                    #cos_similarity.main(lemma, candidate)
                    #print(dic[i][j])
                    #flg = 0
                    flg2 = 1

                #out_put.write('\td:\t[{}]\t'.format(word_pos[1]) + ' '.join(candidate)
                #              + '\t[{}]'.format(word_pos[0]) + '\t{}\n'.format(level))
                #write_inserted(inserted, parent_pos, candidate_num)
                # print(dic[i][j])
                # flg = 0
                #flg2 = 1
                if flg2 == 0:
                    flg = -1
                else:
                    flg = 0

            # 同順連続
            if flg == 2:
                #word_pos, level = search_pos_level(dic[i][j])
                word_pos = search_wordpos(locate, pos)
                if dictionary == 'cefr':
                    level = check_word_level_cefr(dic[i][j], pos, locate)
                elif dictionary == 'evp':
                    level = check_word_level_evp(dic[i][j])
                #簡単な奴は除外
                #if level not in easy_multi:
                out_put.write('\tc:\t' + ' '.join(candidate)
                              + '\t[{}]'.format(word_pos) + '\t{}\n'.format(level))
                # cos_similarity.main(lemma, candidate, out_put)
                search_word2vec.main(candidate, out_put)
                flg2 = 1

                flg = 0
                #flg2 = 1

    if flg == -1:
        out_put.write('\tnotfound\n')
    out_put.write('\n\n')
    #count_in_text[count_text] += 1
    #make_graph(coreference)

def make_dictionary_cefr():
    dic = []
    for i in range(26):
        dic.append([])
        #name = '../make_dict/dic_simple/dic_{}.txt'.format(chr(i+97))
        name = '../make_dict/simple_level2/dic_{}.txt'.format(chr(i + 97))
        #name = 'simple.txt'
        with open(name) as g:
            line = g.readline()
            while line:
                #dic_kari = []
                line = line.replace('\n', '')
                line = line.split('\t')
                words = line[0].split()
                dic[i].append(words)
                line = g.readline()
    return dic

def make_dictionary_evp():
    dic = []

    dic.append([])
    name = '../data/EVP/English_Vocabulary_Profile(EVP)AmE_multi.txt'

    with open(name) as g:
        line = g.readline()
        while line:
            line = line.replace('\n', '')
            line = line.split('\t')
            words = line[1].split()
            dic[0].append(words)
            line = g.readline()
    return dic

def draw_graph(count):
    word, x, y = [], [], []
    for i in range(10):
        x.append(i+1)
        word.append(count[i][0])
        y.append(count[i][1])
    print(word)
    print(y)

    plt.bar(x, y, align='center')
    plt.title("ヒストグラム")
    plt.xticks(x, word)
    plt.show()

def output_data(count, count_in_text):
    x = list(count_in_text)
    with open('output_data.txt', 'w') as out_data:
        for i in range(len(x)):
            out_data.write(str(x[i]) + '\t' + str(count_in_text[x[i]]) + '\n')
        out_data.write('\n')

        for i in range(len(count)):
            out_data.write(str(count[i][1]) + '\t' + str(count[i][0]) + '\n')

def make_dictionary_overlap():
    dic_cefr = []
    for i in range(26):
        name = '../make_dict/simple_level2/dic_{}.txt'.format(chr(i + 97))
        with open(name) as g:
            line = g.readline()
            while line:
                line = line.replace('\n', '')
                line = line.split('\t')
                words = line[0].split()
                dic_cefr.append(words)
                line = g.readline()

    dic = []
    dic.append([])
    name = '../data/EVP/English_Vocabulary_Profile(EVP)AmE_multi.txt'
    with open(name) as g:
        line = g.readline()
        while line:
            line = line.replace('\n', '')
            line = line.split('\t')
            words = line[1].split()
            if words in dic_cefr:
                dic[0].append(words)
            line = g.readline()
    return dic


if __name__ == '__main__':
    #辞書がcefrかevpか
    dictionary = 'overlap'

    #bb = '../practice_core/easy_text.txt'
    if dictionary == 'cefr':
        dic = make_dictionary_cefr()
    elif dictionary == 'evp':
        dic = make_dictionary_evp()
    elif dictionary == 'overlap':
        dic = make_dictionary_overlap()
        dictionary = 'evp'

    count = defaultdict(int)
    count_in_text = defaultdict(int)

    text_candidate = ['economics_sample', 'psychology_sample', 'sociology_sample']
    #for i in range(1):
    for i in text_candidate:
        #out_put_name = 'data2/out_L{}.txt'.format(i+1)
        # out_put_name = 'data4/{}.txt'.format(i)
        # out_put_name = 'data4_evp/{}.txt'.format(i)
        #out_put_name = 'data_xx/out_L{}.txt'.format(i + 1)
        out_put_name = 'out_put.txt'
        with open(out_put_name, 'w') as out_put:

            #text_name = '../data/Kyushutext/xml/L{}.txt.xml'.format(i+1)
            text_name = '../data/Rice_University/xml/{}.txt.xml'.format(i)
            #text_name = '../../../stanford-corenlp-full-2015-01-29/test.txt.xml'
            print(text_name)

            tree = ET.parse(text_name)
            root = tree.getroot()
            sentence = root.findall('document/sentences/sentence')
            aaa = 0
            for sentences in sentence:
                aaa += 1
                #if aaa == 2:
                #    continue

                word_pre = sentences.findall('tokens/token/word')
                lemma_pre = sentences.findall('tokens/token/lemma')
                pos_pre = sentences.findall('tokens/token/POS')
                coreference = sentences.find('dependencies[@type="basic-dependencies"]')
                parse = sentences.find('parse')

                word, lemma, pos = [], [], []

                for i in range(len(word_pre)):
                    word.append(word_pre[i].text)
                    lemma.append(lemma_pre[i].text)
                    pos.append(pos_pre[i].text)
                #if word[0] != 'Economists':
                #    continue
                # 普通
                check(word, lemma, pos, coreference, parse.text, dictionary)
                #コーパスの出現回数を数える
                #()


    #count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    #pprint(count[0:5])
    #pprint(count_in_text)
    #output_data(count, count_in_text)
    #draw_graph(count)
