import matplotlib
import xml.etree.ElementTree as ET
import pos_exchange as pos_ex
matplotlib.rcParams["font.family"] = 'TakaoPGOthic'
from graphviz import Digraph


def map_all(es):
    return all([e == es[0] for e in es[1:]]) if es else False

def make_tree(parse):
    G = Digraph(format='png')
    G.attr('node', shape='circle')
    depth = 0
    maximum = 0
    number = 0
    labeling = [str(number)]
    G.node(labeling[0], 'ROOT')
    parse.pop(0)
    parent = [-1]

    for word in parse:
        number += 1
        depth += 1
        parent.append(labeling[depth-1])
        if word[0] == '(':
            word = word.replace('(', '')
            if len(labeling) <= depth:
                labeling.append(str(number))
            else:
                labeling[depth] = str(number)
            G.node(labeling[depth], word)
            G.edge(labeling[depth-1], labeling[depth])

        elif word[-1] == ')':
            count = word.count(')') + 1
            word = word.rstrip(')')

            if len(labeling) <= depth:
                labeling.append(str(number))
            else:
                labeling[depth] = str(number)

            G.node(labeling[depth], word)
            G.edge(labeling[depth-1], labeling[depth])
            depth -= count

        if maximum < depth:
            maximum = depth

    #G.render(view=True)
    for i in range(len(parent)):
        parent[i] = int(parent[i])

    return parent

def search_parent(parent, index2, parse):
    same_parent = []
    index = index2.copy()
    #print(index)
    for j in range(len(index)):
        i = index[j].copy()
        while 1:
            i.sort()
            i[-1] = int(parent[i[-1]])
            if map_all(i):
                #if i[0] not in same_parent:
                same_parent.append(i[0])
                break
    parent_pos = []
    for i in same_parent:
        parent_pos.append(parse[i])
    #print(index)
    return parent_pos, same_parent

def search_index(parse, words, lemma, word):
    index_kari = []
    index = []
    for i in words:
        number_kari = [aaa for aaa, x in enumerate(lemma) if x == i]
        index_kari.append([])
        for j in number_kari:
            index_kari_kari = [bbb for bbb, x in enumerate(parse) if x == word[j]]
            index_kari[-1] = index_kari[-1] + index_kari_kari
    if len(words) == 2:
        for i in range(len(index_kari[0])):
            kari = [index_kari[0][i]]
            for j in range(len(index_kari[1])):
                if index_kari[0][i] < index_kari[1][j]:
                    kari2 = kari.copy()
                    kari2.append(index_kari[1][j])
                    index.append(kari2)
    if len(words) == 3:
        for i in range(len(index_kari[0])):
            kari = [index_kari[0][i]]
            for j in range(len(index_kari[1])):
                if index_kari[0][i] < index_kari[1][j]:
                    kari2 = kari.copy()
                    kari2.append(index_kari[1][j])
                    for k in range(len(index_kari[2])):
                        if index_kari[1][j] < index_kari[2][k]:
                            kari3 = kari2.copy()
                            kari3.append(index_kari[2][k])
                            index.append(kari3)
    if len(words) == 4:
        #print(words)
        #print(index_kari)
        for i in range(len(index_kari[0])):
            kari = [index_kari[0][i]]
            for j in range(len(index_kari[1])):
                if index_kari[0][i] < index_kari[1][j]:
                    kari2 = kari.copy()
                    kari2.append(index_kari[1][j])
                    for k in range(len(index_kari[2])):
                        if index_kari[1][j] < index_kari[2][k]:
                            kari3 = kari2.copy()
                            kari3.append(index_kari[2][k])
                            for l in range(len(index_kari[3])):
                                if index_kari[2][k] < index_kari[3][l]:
                                    kari4 = kari3.copy()
                                    kari4.append(index_kari[3][l])
                                    index.append(kari4)
    if len(words) == 5:
        for i in range(len(index_kari[0])):
            kari = [index_kari[0][i]]
            for j in range(len(index_kari[1])):
                if index_kari[0][i] < index_kari[1][j]:
                    kari2 = kari.copy()
                    kari2.append(index_kari[1][j])
                    for k in range(len(index_kari[2])):
                        if index_kari[1][j] < index_kari[2][k]:
                            kari3 = kari2.copy()
                            kari3.append(index_kari[2][k])
                            for l in range(len(index_kari[3])):
                                if index_kari[2][k] < index_kari[3][l]:
                                    kari4 = kari3.copy()
                                    kari4.append(index_kari[3][l])
                                    for m in range(len(index_kari[4])):
                                        if index_kari[3][l] < index_kari[4][m]:
                                            kari5 = kari4.copy()
                                            kari5.append(index_kari[4][m])
                                            index.append(kari5)
    return index

def search_insert(parse, index, same_parent, parent):
    #parse = parse.split()
    insert = []
    if len(index) != len(same_parent):
        print("AAAAAA")
    #print(index)
    for i in range(len(index)):
        interval_kari = []
        for j in range(len(index[i])-1):
            interval_kari_kari = []
            left_ori, right_ori = index[i][j], index[i][j + 1]
            left, right = index[i][j], index[i][j+1]
            count = 0
            pre_left, pre_right = [left], [right]
            while parent[left] != same_parent[i]:
                left = parent[left]
                pre_left.append(left)
                #print(left, right)
                for k in range(left_ori+1, right):
                    if parent[k] == left and k not in pre_left:
                        interval_kari_kari.append(parse[k])
                        count += 1

            while parent[right] != same_parent[i]:
                right = parent[right]
                pre_right.append(right)
                for k in range(right_ori-1, left, -1):
                    if parent[k] == right and k not in pre_right:
                        interval_kari_kari.insert(count, parse[k])
            for k in range(left_ori+1, right_ori):
                if parent[k] == same_parent[i]:
                    if k != left and k != right:
                        interval_kari_kari.insert(count, parse[k])
            interval_kari.append(interval_kari_kari)
        insert.append(interval_kari)
    '''
    for i in range(len(insert)):
        for j in range(len(insert[i])):
            for k in range(len(insert[i][j])):
                insert[i][j][k] = pos_ex.pos_exchange_parse(insert[i][j][k])
    '''

    return insert



def main_tree(word, lemma, pos, parse, words):
    parse_words = parse
    parse_words = parse_words.replace('(', '')
    parse_words = parse_words.replace(')', '')
    parent = make_tree(parse.split())
    #search_indexで1つ以上の複合語の候補のインデックスを返す
    index = search_index(parse_words.split(), words, lemma, word)
    #print(index)
    parent_pos, same_parent = search_parent(parent, index, parse_words.split())
    #parent_pos = parse_words.split()[same_parent]
    #print(index)
    insert = search_insert(parse_words.split(), index, same_parent, parent)
    return parent_pos, insert, index


if __name__ == '__main__':

    text_name = '../data/Kyushutext/xml/L{}.txt.xml'.format(2)
    tree = ET.parse(text_name)
    root = tree.getroot()
    sentence = root.findall('document/sentences/sentence')
    aaa = 0
    for sentences in sentence:
        aaa += 1
        if aaa!= 52:
            continue
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

        words = ['the', 'two']
        parent_pos, insert = main_tree(word, lemma, pos, parse, words)
        print(parent_pos)
        print(insert)
        break
