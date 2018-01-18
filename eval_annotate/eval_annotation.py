from sklearn.metrics import cohen_kappa_score
import itertools

def get_data(people_list):
    cs, judge = [], []
    judge_0 = []
    judge_unk = []

    for people in people_list:
        text_name = 'result/annotate1_{}.txt'.format(people)

        cs_kari = []

        judge_0_kari = 0
        judge_unk_kari = 0

        with open(text_name, 'r', encoding='utf-8', errors='ignore') as f:
            line = f.readline()
            line = line.split('\t')
            while line != ['']:
                line2 = f.readline()
                line2 = line2.split('\t')

                while line[0] == line2[0]:
                    line2 = f.readline()
                    line2 = line2.split('\t')

                if line[6] == 'C.S.':
                    pass
                elif line[6] == '1':
                    cs_kari.append(1)
                elif line[6] == '':
                    cs_kari.append(0)
                else:
                    cs_kari.append(2)

                if line[7] == '0':
                    judge_0_kari += 1

                line = line2
        cs.append(cs_kari)

        judge_kari = []
        with open(text_name, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.split('\t')
                if line[7] == 'judge':
                    pass
                # 言い換え可
                elif line[7] == '1':
                    judge_kari.append(1)
                # 言い換え不可
                elif line[7] == '':
                    judge_kari.append(0)
                # そもそも複合語じゃない
                elif line[7] == '0':
                    judge_kari.append(2)
                # 判別不能
                else:
                    judge_unk_kari += 1
                    judge_kari.append(3)


        judge.append(judge_kari)
        judge_0.append(judge_0_kari)
        judge_unk.append(judge_unk_kari)

    return cs, judge, judge_0, judge_unk

def print_data(cs, judge, judge_0, people_list):
    for i in range(len(people_list)):
        print(people_list[i])
        print('C.S.判定')
        print('推測可\t\t{}'.format(cs[i].count(0)))
        print('推測不可\t\t{}'.format(cs[i].count(1)))
        print('判断不可\t\t{}'.format(cs[i].count(2)))
        print('judge判定')
        print('言い換え可\t\t{}'.format(judge[i].count(1)))
        print('言い換え不可\t\t{}'.format(judge[i].count(0)))
        print('複合語じゃない\t{}({})'.format(judge_0[i], judge[i].count(2)))
        print('言い換え判定難\t{}'.format(judge[i].count(3)))
        print()

def calc_kappa(data, category):

    small_p, capital_p = [], []
    total_cand = len(data[0])
    people_num = len(data)


    for j in range(category):
        small_p_kari = 0
        for i in range(total_cand):
            for k in range(people_num):
                if data[k][i] == j:
                    small_p_kari += 1
        small_p.append(small_p_kari/(total_cand*people_num))

    for i in range(total_cand):
        capital_p_kari = []

        for j in range(category):
            capital_p_kari_kari = 0
            for k in range(people_num):
                if data[k][i] == j:
                    capital_p_kari_kari += 1
            capital_p_kari.append(capital_p_kari_kari)

        capital_p_kari_kari = -1*people_num
        for j in range(category):
            capital_p_kari_kari += capital_p_kari[j]*capital_p_kari[j]
        capital_p.append(capital_p_kari_kari/(people_num*(people_num-1)))

    cap_p_bar = 0
    for i in range(total_cand):
        cap_p_bar += capital_p[i]
    cap_p_bar = cap_p_bar / total_cand

    cap_p_bar_e = 0
    for i in range(category):
        cap_p_bar_e += small_p[i]*small_p[i]

    kappa = (cap_p_bar-cap_p_bar_e)/(1-cap_p_bar_e)

    return kappa

def kappa_check():
    data = [[5, 2, 3, 2, 1, 1, 1, 1, 1, 2],
            [5, 2, 3, 2, 1, 1, 1, 1, 1, 2],
            [5, 3, 3, 2, 2, 1, 1, 2, 1, 3],
            [5, 3, 4, 3, 2, 1, 2, 2, 1, 3],
            [5, 3, 4, 3, 3, 1, 2, 2, 1, 4],
            [5, 3, 4, 3, 3, 1, 3, 2, 1, 4],
            [5, 3, 4, 3, 3, 1, 3, 2, 2, 4],
            [5, 3, 4, 3, 3, 2, 3, 3, 2, 5],
            [5, 4, 5, 3, 3, 2, 3, 3, 2, 5],
            [5, 4, 5, 3, 3, 2, 3, 3, 2, 5],
            [5, 4, 5, 3, 3, 2, 3, 4, 2, 5],
            [5, 4, 5, 3, 3, 2, 4, 4, 3, 5],
            [5, 5, 5, 4, 4, 2, 4, 5, 3, 5],
            [5, 5, 5, 4, 5, 2, 4, 5, 4, 5],
            ]

    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] -= 1
    kappa = calc_kappa(data, 5)

    print(kappa)

def write_data(cs, judge, judge_0, people_list):
    out_data = 'annotate_eval.txt'
    with open(out_data, 'w') as out:
        for i in range(len(people_list)):
            out.write('{}\n'.format(people_list[i]))
            out.write('C.S.判定\n')
            out.write('推測可\t{}\n'.format(cs[i].count(0)))
            out.write('推測不可\t{}\n'.format(cs[i].count(1)))
            out.write('判断不可\t{}\n'.format(cs[i].count(2)))
            out.write('judge判定\n')
            out.write('言い換え可\t{}\n'.format(judge[i].count(1)))
            out.write('言い換え不可\t{}\n'.format(judge[i].count(0)))
            out.write('複合語じゃない\t{}({})\n'.format(judge_0[i], judge[i].count(2)))
            out.write('言い換え判定難\t{}\n\n'.format(judge[i].count(3)))

def write_cohen(dic_cs, dic_judge, data):
    out_name = 'cohen.txt'
    with open(out_name, 'w') as out:
        for people1, people2 in data:
            out.write('{}\t{}\n'.format(people1, people2))
            out.write('C.S.\t{}\n'.format(cohen_kappa_score(dic_cs[people1], dic_cs[people2])))
            out.write('judge.\t{}\n\n'.format(cohen_kappa_score(dic_judge[people1], dic_judge[people2])))


def cohen_kappa(people_list, cs, judge):
    dic_cs, dic_judge = {}, {}
    for i in range(len(people_list)):
        dic_cs.update({people_list[i]:cs[i]})
        dic_judge.update({people_list[i]: judge[i]})

    data = list(itertools.combinations(people_list,2))
    for people1, people2 in data:
        print(people1, people2)
        print('C.S.\t{}'.format(cohen_kappa_score(dic_cs[people1], dic_cs[people2])))
        print('judge.\t{}'.format(cohen_kappa_score(dic_judge[people1], dic_judge[people2])))
        print()

    write_cohen(dic_cs, dic_judge, data)






if __name__ == '__main__':

    people_list = ['haswell', 'vani_devi', 'wombat19']
    cs, judge, judge_0, judge_unk = get_data(people_list)

    # print_data(cs, judge, judge_0, people_list)
    # write_data(cs, judge, judge_0, people_list)


    # ここから下はkappa値を求めている。

    # # まずはfleiss kappa
    # # kappa_check()
    #
    # kappa_cs = calc_kappa(cs, 3)
    # kappa_judge = calc_kappa(judge, 4)
    #
    # print('C.S.\t{}'.format(kappa_cs))
    # print('judge \t{}'.format(kappa_judge))

    # 次にcohen kappa
    cohen_kappa(people_list, cs, judge)






