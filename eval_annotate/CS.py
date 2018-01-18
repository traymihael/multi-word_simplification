def cs_reverse(input_name, save_name):
    with open(input_name, 'r', encoding='utf-8', errors='ignore') as f, open(save_name, 'w') as out:
        for line in f:
            line = line.split('\t')
            if line[6] == '':
                line[6] = '1'
            elif line[6] == '1':
                line[6] = ''
            out.write('\t'.join(line))


def cs_extend(input_name, save_name):
    with open(input_name, 'r', encoding = 'utf-8',errors = 'ignore') as f, open(save_name, 'w') as out:
        line = f.readline()
        line = line.split('\t')
        while line != ['']:
            data = []
            data.append(line)
            line2 = f.readline()
            line2 = line2.split('\t')

            while line[0] == line2[0]:
                data.append(line2)
                line2 = f.readline()
                line2 = line2.split('\t')

            for i in range(len(data)):
                if data[i][6] == '1':
                    for j in range(len(data)):
                        data[j][6] = '1'
                    break

            for i in range(len(data)):
                out.write('\t'.join(data[i]))

            line = line2


if __name__ == '__main__':
    # # vani_deviさんはreverse
    # # pop the questionに1を入れたい
    # people = 'vani_devi'
    #
    # texe_name = 'annotate1_{}.txt'.format(people)
    # input_name = 'result_original/{}'.format(texe_name)
    # save_name = 'result2/{}'.format(texe_name)
    # cs_reverse(input_name, save_name)

    # # wombatさんはCS判定の際一番上に1をつけているのみなので
    # # それを下まで
    # people = 'wombat19'
    #
    # texe_name = 'annotate1_{}.txt'.format(people)
    # input_name = 'result_original/{}'.format(texe_name)
    # save_name = 'result2/{}'.format(texe_name)
    #
    # cs_extend(input_name, save_name)
