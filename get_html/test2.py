import pprint
import json
import corenlp

# パーサの生成
corenlp_dir = '/home/ashihara/stanford-corenlp-full-2013-06-20/'
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

# パースして結果をpretty print
result_json = json.loads(parser.parse('I ate tomatos.'))
pprint.pprint(result_json)