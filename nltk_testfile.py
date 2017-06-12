import nltk
from nltk.tokenize import PunktSentenceTokenizer

train_text = open("123.txt","r").read()
sample_text = open("got.txt","r").read()

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[1:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            print (namedEnt)
    except Exception as e:
        print(str(e))


process_content()

