import csv
import pprint

def search(word):
    with open('CEFR_level_list.csv', 'r') as f:
        reader = csv.reader(f)
        #header = next(reader)  # ヘッダーを読み飛ばしたい時

        for row in reader:
            if row[0] == word:
                print(word, '\t', 'is', row[1], '\t', 'and rank is', row[2])
                return

        print(word, '\t', 'can not find')

with open('test.txt') as f:
    sentence = f.readline()
    # パースして結果をpretty print
    while sentence:
        sentence = sentence.split()
        for word in sentence:
            search(word)

        sentence = f.readline()




