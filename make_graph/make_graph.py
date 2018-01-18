import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = 'TakaoPGOthic'

def graph1(x_bar, x, y):
    plt.bar(x_bar, y, align='center')
    plt.title('Number of multi-word in a sentence and Occurrences')
    plt.xticks(x_bar, x)
    plt.xlabel('Number of multi-word in a sentence')
    plt.ylabel('Occurrences')
    plt.savefig('graph4.png')
    plt.show()

def graph2(x_bar, x, y):
    plt.bar(x_bar, y, align='center')
    plt.title('Number of multi-word in a sentence and Occurrences')
    plt.xticks(x_bar, x)
    plt.xlabel('Number of multi-word in a sentence')
    plt.ylabel('Occurrences')
    plt.savefig('graph5.png')
    plt.show()

def graph3(x_bar, x, y):
    plt.bar(x_bar, y, align='center')
    plt.title('multi-word and Occurrences')
    plt.xticks(x_bar, x)
    plt.xlabel('multi-wrd')
    plt.ylabel('Occurrences')
    plt.savefig('graph6.png')
    plt.show()


if __name__ == '__main__':
    with open('../text_matching/output_data_more2.txt') as f:
        line = f.readline()
        count = []
        while line != '\n':
            line = line.split()
            point1 = int(line[0])
            point2 = int(line[1])
            count.append([point1, point2])
            line = f.readline()

        line = f.readline()
        with open('Occurrences.csv', 'w') as g:
            how_many = 10
            count_time = 0
            x_occ_bar, x_occ, y_occ = [], [], []
            while '\t' in line:
                count_time += 1

                line = line.replace('\t', ',')
                g.write(line)

                if count_time <= how_many:
                    line2 = line.split(',')
                    x_occ_bar.append(count_time)
                    x_occ.append(line2[1].replace('\n', ''))
                    y_occ.append(int(line2[0]))

                line = f.readline()

    count_sort = sorted(count, key=lambda x: x[0])
    count = sorted(count, key=lambda x: x[1], reverse=True)
    x_bar, x, y, x_sort, y_sort = [], [], [], [], []
    for i in range(len(count)):
        x_bar.append(i+1)
        x.append(count[i][0])
        y.append(count[i][1])
        x_sort.append(count_sort[i][0])
        y_sort.append(count_sort[i][1])

    graph1(x_bar, x, y)
    graph2(x_bar, x_sort, y_sort)
    graph3(x_occ_bar, x_occ, y_occ)