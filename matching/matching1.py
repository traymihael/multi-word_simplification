from pprint import pprint
import time

start_time = time.time()


with open('../get_multi/phrase_verb.txt') as g:
    data = []
    count_all1 = 0

    line = g.readline().split('*')
    while line:
        count_all1 += 1
        data.append(line[0].split())
        #print(line)
        line = g.readline().split('*')
        if len(line) != 2:
            break
    #pprint(data)


text_name1 = '../data/syn_data_'
text_name3 = '.txt'
check2 = 'a'
count_all = 0
count_match = 0
error_text = 0

with open('matching_list_phrase_verb.txt', 'w') as text:
    for i in range(26):
        text_name2 = chr(97+i)
        text_name = text_name1 + text_name2 + text_name3
        print(text_name)
        count_all += 1

        with open(text_name) as f:

            line2 = f.readline()
            while line2:
                line2 = line2.split('\t')
                check = line2[0].split()
                if check in data:
                    if check2 != check:
                        for k in range(len(check)):
                            text.writelines(check[k])
                            text.writelines(' ')

                        text.writelines('\n')
                        check2 = check
                        count_match += 1

                try:
                    line2 = f.readline()
                except:
                    #print('Error')
                    error_text += 1
                    line2 = ''

print('number of data = ', count_all1)
print('match data = ', count_match)
print('error text = ', error_text)


end_time = time.time()
interval = end_time - start_time
print(str(interval), "秒")
