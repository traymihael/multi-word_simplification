import pprint
import json
import corenlp

# パーサの生成
corenlp_dir = "/home/ashihara/stanford-corenlp-full-2015-01-29/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

# パースして結果をpretty print
# result_json = json.loads(parser.parse("I am Alice."))
# pprint.pprint(result_json)