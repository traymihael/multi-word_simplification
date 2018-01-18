import re
def check_phrase(line3):
    phrase = ['ADJP', 'ADVP', 'NP']
    pos_line = re.search('\[\((.*?)\)\]', line3)
    for pos in phrase:
        if pos == pos_line.group(1):
            return 1
    return 0

def check_phrase2(line2):
    line = line2.replace('\n', '')
    line = line.split('\t')
    index = line[5].split(',')
    for i in range(len(index)):
        if index[i] == '???':
            return 0
        index[i] = int(index[i])
    for i in range(len(index)-1):
        left = index[i]
        right = index[i+1]
        if right - left > 2:
            return 1
    return 0

def write_result(input_name, out_name):
    with open(input_name, 'r') as f, open(out_name, 'w') as out:
        line = f.readline()
        while line:
            flg = 1
            line2 = f.readline()
            line3 = f.readline()
            while line2 != '\n':
                # # 挿入句の品詞で判断
                # if check_phrase(line3):
                # 複合語がどれだけ離れているかで判断
                if check_phrase2(line2):
                    if flg:
                        out.write(line)
                        flg = 0
                    out.write(line2)
                    out.write(line3)
                line2 = f.readline()
                line3 = f.readline()
            line = line3
            if flg == 0:
                out.write('\n')


if __name__ == '__main__':
    mode = 'intro'
    input_name = '{}.txt'.format(mode)
    out_name = '{}_more2.txt'.format(mode)
    write_result(input_name, out_name)