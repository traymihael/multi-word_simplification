cd '../../../stanford-corenlp-full-2015-01-29'
command='java -cp stanford-corenlp-3.5.1.jar:stanford-corenlp-3.5.1-models.jar:xom.jar:joda-time.jar:slf4j-api.jar:jollyday.jar -Xmx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file 1-0.txt'
eval $command
