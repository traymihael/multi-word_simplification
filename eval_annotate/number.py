if __name__ == '__main__':
    people = 'haswell'

    texe_name = 'annotate1_{}.txt'.format(people)
    input_name = 'result_original/{}'.format(texe_name)
    save_name = 'result2/{}'.format(texe_name)

    with open(input_name, 'r', encoding = 'utf-8',errors = 'ignore') as f, open(save_name, 'w') as out:
        count = 0
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
                if count == 0:
                    out.write('\t'.join(data[i]))
                    break
                data[i][0] = str(count)
                out.write('\t'.join(data[i]))

            line = line2
            count += 1

        print(count)