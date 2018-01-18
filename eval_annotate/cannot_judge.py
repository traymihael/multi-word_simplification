if __name__ == '__main__':
    people_list = ['haswell', 'vani_devi', 'wombat19']

    for people in people_list:
        text_name = 'result2/annotate1_{}.txt'.format(people)
        out_name = 'result/annotate1_{}.txt'.format(people)

        with open(text_name, 'r', encoding='utf-8', errors='ignore') as f, open(out_name, 'w') as out:

            line = f.readline()
            while line:
                data = []
                line_kari = line.split('\t')
                data.append(line_kari)
                target_num = line_kari[0]
                line2 = f.readline()
                line2_kari = line2.split('\t')
                target2_num = line2_kari[0]

                while target_num == target2_num:
                    data.append(line2_kari)
                    line2 = f.readline()
                    line2_kari = line2.split('\t')
                    target2_num = line2_kari[0]

                for i in range(len(data)):
                    if data[i][7] == '0':
                        for j in range(len(data)):
                            data[j][7] = '0'
                        break

                for i in range(len(data)):
                    out.write('\t'.join(data[i]))

                line = line2
