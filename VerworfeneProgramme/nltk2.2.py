
#--------------------------------------------------------------------------------------------------------------------
#deleted the function and added explanations for each line
#--------------------------------------------------------------------------------------------------------------------
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords

raw_text = open("got.txt", "r").read()


#Tokenizer laden
custom_sent_tokenizer = PunktSentenceTokenizer()
#->Liste mit Teilstrings der einzelnen Sätze
tokenized = custom_sent_tokenizer.tokenize(raw_text)

for i in tokenized:
    #Jedes Wort als einzelnen String in Liste
    words = nltk.word_tokenize(i)
    #Jedes Wort mit POS-Tag in Liste
    tagged = nltk.pos_tag(words)
    #Jeder Satz als Tree mit POS-Tag
    namedEnt = nltk.ne_chunk(tagged, binary=True)
    #Speichern des regulären Ausdrucks
    chunkGram = r"""Chunk: {<NE>+<.*>*<VB.?>+<.*>*<NE>|<PRP>+<.*>*<VB.?>+<.*>*<NE>}"""
    #ChunkParser laden
    chunkParser = nltk.RegexpParser(chunkGram)
    #Speichern der chunking Treffer als Tree
    chunked = chunkParser.parse(namedEnt)
    #erstellen und einfügen in eine Liste für chunking Treffer
    docs = []
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                docs.append(" ".join([a for (a,b) in subtree.leaves()]))
                #subtree.draw()
    for i in docs:
        print(i)
        
#---------------------------------------------------------------------    
##    kill_list = set(["kill", "die", "stab", "murder", "dead"])
##    kill_sentence= [w for w in docs if not w in kill_list]
##    for i in kill_sentence:
##        print(i)
