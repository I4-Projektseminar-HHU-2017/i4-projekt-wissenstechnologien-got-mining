import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords

raw_text = open("got1.txt", "r").read()
namedEnttxt = open("got1NE.txt", "w")

#Tokenizer laden
custom_sent_tokenizer = PunktSentenceTokenizer()
#->Liste mit Teilstrings der einzelnen Sätze
tokenized = custom_sent_tokenizer.tokenize(raw_text)
docs = []
docs2 = []
for i in tokenized:
    #Jedes Wort als einzelnen String in Liste
    words = nltk.word_tokenize(i)
    #Jedes Wort mit POS-Tag in Liste
    tagged = nltk.pos_tag(words)
    #Jeder Satz als Tree mit POS-Tag
    namedEnt = nltk.ne_chunk(tagged, binary=False)
    #Speichern des regulären Ausdrucks
    chunkGram = r"""Chunk: {<PERSON>}"""
    #ChunkParser laden
    chunkParser = nltk.RegexpParser(chunkGram)
    #Speichern der chunking Treffer als Tree
    chunked = chunkParser.parse(namedEnt)
    #erstellen und einfügen in eine Liste für chunking Treffer
    
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                docs.append(" ".join([a for (a,b) in subtree.leaves()]))
                #subtree.draw()
for i in docs:
    if(i not in docs2):
        docs2.append(i)
    else:
        continue
for line in docs2:
    namedEnttxt.write(line+".")
namedEnttxt.close()
print("finished")
    

#---------------------------------------------------------------------
##    kill_example = ["I will kill you.", "I guess i will die.", "I like rainbows."]           
##    kill_list = set(["kill", "die", "stab", "murder", "dead"])
##    kill_sentence= [w for w in kill_example if w in kill_list]
##    print(kill_sentence)
