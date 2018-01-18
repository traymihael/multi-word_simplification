import os
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
import sys
sys.path.append('../word2vec')
import search_word2vec
sys.path.append('../Doc2vec')
import doc2vec_search2
sys.path.append('../Tfidf')
import tfidfvector
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

def search_index(lemma, multiword):
    for j in range(len(lemma)):
        index = [[]]
        if multiword[0] == lemma[j]:
            for k in range(len(multiword)):
                if multiword[k] != lemma[j+k]:
                    break
                index[0].append(j+k)
            if len(index[0]) == len(multiword):
                return index

def check(word, lemma, pos, parse, dictionary):
    # out_put.write(' '.join(word) + '\n')
    flg, flg2 = -1, 0
    flg3 = 1

    for i in range(len(dic)):
        for j in range(len(dic[i])):
            locate = []
            locate_coount = 0

            #同順非連続
            if len(set(dic[i][j])) == len(set(dic[i][j]) & set(lemma)):
                verif = lemma.copy()

                for k in range(len(dic[i][j])):
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
                word_pos = search_wordpos(locate, pos)
                parent_pos, inserted, multi_index = search_tree.main_tree(word, lemma, pos, parse, dic[i][j])
                candidate_num, flg_ins = judge_insert.inserte_check(word_pos.split(), inserted)
                try:
                    for index_number in range(len(multi_index[0])):
                        multi_index[0][index_number] = str(multi_index[0][index_number])
                except:
                    pass
                if dictionary == 'cefr':
                    level = check_word_level_cefr(dic[i][j], pos, locate)
                elif dictionary == 'evp':
                    level = check_word_level_evp(dic[i][j])

                if flg_ins:
                    if flg3:
                        out_put.write(' '.join(word) + '\n')
                        flg3 = 0
                    # print(multi_index[0])
                    out_put.write('\td:\t' + ' '.join(candidate)
                                  + '\t[{}]'.format(word_pos) + '\t{}\t{}\n'.format(level, ','.join(multi_index[0])))
                    # write_inserted(inserted, parent_pos, candidate_num)
                    # doc2vec_search2.main(word, candidate, multi_index, out_put)

                    flg2 = 1

                if flg2 == 0:
                    flg = -1
                else:
                    flg = 0

            # 同順連続
            if flg == 2:
                multi_index = search_index(lemma, dic[i][j])
                try:
                    for index_number in range(len(multi_index[0])):
                        multi_index[0][index_number] = str(multi_index[0][index_number])
                except:
                    flg2 = 1
                    flg = 0
                    continue

                word_pos = search_wordpos(locate, pos)
                if dictionary == 'cefr':
                    level = check_word_level_cefr(dic[i][j], pos, locate)
                elif dictionary == 'evp':
                    level = check_word_level_evp(dic[i][j])
                if flg3:
                    out_put.write(' '.join(word) + '\n')
                    flg3 = 0
                out_put.write('\tc:\t' + ' '.join(candidate)
                              + '\t[{}]'.format(word_pos) + '\t{}\t{}\n'.format(level, ','.join(multi_index[0])))
                # doc2vec_search2.main(word, candidate, multi_index, out_put)
                # tfidfvector.main(word, candidate, multi_index, out_put)
                # print(multi_index)
                search_word2vec.main(candidate, out_put)
                # print(candidate)

                flg2 = 1

                flg = 0

    # if flg == -1:
    #     out_put.write('\tnotfound\n')
    if flg3 == 0:
        out_put.write('\n')
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
    dic = []
    dic.append([])
    name = '../data/EVP/overlap_dict.txt'
    with open(name) as g:
        line = g.readline()
        while line:
            line = line.replace('\n', '')
            line = line.split('\t')
            words = line[1].split()
            dic[0].append(words)
            line = g.readline()
    return dic

def pre_main(text_name, dictionary):
    with open(text_name, 'r', encoding='utf-8', errors='ignore') as in_put:
        line = in_put.readline()
        while line:
            # try:
            line2 = in_put.readline()
            line3 = in_put.readline()
            line4 = in_put.readline()

            line = line.replace('\n', '')
            line2 = line2.replace('\n', '')
            line3 = line3.replace('\n', '')
            line4 = line4.replace('\n', '')
            word, lemma, pos, parse = line.split(), line2.split(), line3.split(), line4
            check(word, lemma, pos, parse, dictionary)
            while line != '\n':
                line = in_put.readline()
            line = in_put.readline()

if __name__ == '__main__':
    #辞書がcefrかevpか
    dictionary = 'overlap'

    if dictionary == 'cefr':
        dic = make_dictionary_cefr()
    elif dictionary == 'evp':
        dic = make_dictionary_evp()
    elif dictionary == 'overlap':
        dic = make_dictionary_overlap()
        dictionary = 'evp'

    text_candidate = ['economics', 'psychology', 'sociology']


    out_put_name = 'out_put.txt'
    with open(out_put_name, 'w') as out_put:
        for i in text_candidate:
            text_name = '../data/Rice_University/Intro/{}_sample2.txt'.format(i)
            print(text_name)
            pre_main(text_name, dictionary)

    # for i in text_candidate:
    #     out_put_name = 'Rice_text/1/{}.txt'.format(i)
    #     files = os.listdir('../data/Rice_University/{}/{}_morph'.format(i, i))
    #
    #     with open(out_put_name, 'w') as out_put:
    #         for file in files:
    #             text_name = '../data/Rice_University/{}/{}_morph/{}'.format(i, i, file)
    #             pre_main(text_name, dictionary)

