from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = 'TakaoPGOthic'


def pre_ready(count_multi):
    text_name = '../data/Rice_University/overlap_data.txt'
    with open(text_name, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split('\t')
            count_multi[line[2]] += int(line[1])


def marge_data(text_name):
    with open(text_name) as f:
        for line in f:
            line = line.replace('\n', '')
            words, number = line.split('\t')
            count_multi[words] += int(number)


def draw_graph(count):
    # count = defaultdict(int)
    word, x, y = [], [], []
    # for i in range(len(count_multi)):
    #     number = count_multi[i][1]
    #     count[int(number)] += 1
    # count = sorted(count.items(), key=lambda x: x[0])
    #
    # with open('../corpus4/frequence.txt', 'w') as out_put:
    #     for i in range(len(count)):
    #         out_put.write(str(count[i][0]) + '\t' + str(count[i][1]) + '\n')

    for i in range(len(count)):
        x.append(i + 1)
        word.append(count[i][0])
        y.append(count[i][1])
    # print(word)
    # print(y)

    plt.bar(x, y, align='center')
    plt.title("出現した複合語の回数（CEFR）")
    plt.xticks(x, word)
    plt.show()


if __name__ == '__main__':
    count_multi = defaultdict(int)
    pre_ready(count_multi)
    count_multi = sorted(count_multi.items(), key=lambda x: x[1], reverse=True)
    # count_multi2 = [('A1',count_multi['A1']),('A2',count_multi['A2']),('B1',count_multi['A1']),
    #                 ('B2', count_multi['A1']),('C1',count_multi['A1']),('C2',count_multi['A1'])]
    # count_multi = sorted(count_multi.items(), key=lambda x: x[1], reverse=True)
    # print(count_multi)
    # print(count_multi2)
    # out_put_name = '../corpus4/count_count.txt'
    # with open(out_put_name, 'w') as out_put:
    #      for i in range(len(count_multi)):
    #          out_put.write(count_multi[i][0] + '\t' + str(count_multi[i][1]) + '\n')

    draw_graph(count_multi)


