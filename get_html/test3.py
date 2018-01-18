import pprint
import json
import corenlp

# パーサの生成
corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
properties_file = "./user.properties"
parser = corenlp.StanfordCoreNLP(
    corenlp_path=corenlp_dir,
    properties=properties_file) # propertiesを設定

with open('test.txt') as f:
    sentence = f.readline()
    # パースして結果をpretty print
    while sentence:
        result_json = json.loads(parser.parse(sentence))
        pprint.pprint(result_json)
        sentence = f.readline()