from pprint import pprint
import json
import corenlp

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

#辞書の読み込み
def read_idiomdata(data_name):
    lis = []
    with open(data_name, 'r') as f:
        line = f.readline().split('*')
        i = 0
        while line:
            try:
                lis.append([line[0].split(), line[1]])
                line = f.readline().split('*')
            except:
                break
    return lis

#表示
def print_sentence(sentence):
    for j in range(1):
        for i in range(len(sentence[j])):
            print(sentence[j][i],end=' ')
        print()

#イディオムの検索
def check(sentence, lis):
    for i in range(len(sentence)):
        #print(sentence[i])
        #print_sentence(sentence[i])
        for j in range(len(lis)):
            flg = 0
            #if set(lis[j][0]) == set(sentence[i]):
            if len(set(lis[j][0]) & set(sentence[i][1])) == len(lis[j][0]):
                #print('ok')
                print_sentence(sentence[i])
                print(lis[j][0],'=',lis[j][1])
                #print(set(lis[j][0]) & set(sentence[i]),len(lis[j]))
                flg = 1
                #print('')
                break
        #if flg == 0:
            #print('NOT FOUND')
        #print('')
    #print('NOT FOUND')



#一文、単語ごとへの分割
def split_sentence(text_name):
    sentence = []
    with open(text_name) as NLP:
        try:
            for line in NLP:
                if line != '\n':
                    sentence.append([[],[]])
                    #print(line)
                    #pprint(parser.raw_parse(line))
                    #print('----')
                    #print(line)
                    #print(parser.raw_parse(line)["sentences"][0]["words"])
                    #pprint(parser.raw_parse(line)["sentences"][0])
                    for i in parser.raw_parse(line)["sentences"][0]["words"]:
                        #print(i[0] + "\t" + str(i[1]["Lemma"]) + "\t" + i[1]["PartOfSpeech"])
                        sentence[-1][0].append(i[0])
                        sentence[-1][1].append(i[1]["Lemma"])
        except:
            pass
        return sentence

if __name__ == '__main__':
    print('------')
    lis = read_idiomdata('idiom_clean.csv')
    sentence = split_sentence('easy_text.txt')
    #pprint(sentence)
    check(sentence, lis)

