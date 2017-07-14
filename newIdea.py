import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords

#Beispieltext einlesen
raw_text = open("buch.txt", "r").read()

#Liste mit Synonymen einlesen
synonym_text = open("synonyms.txt", "r").read()
#Synonym-Liste tokenizen
synonyms = nltk.word_tokenize(synonym_text)

#Liste mit gefundenen Sätzen für später
sentenceList = ([])
verbs = ([])
#print(synonyms)

#Tokenizer laden
custom_sent_tokenizer = PunktSentenceTokenizer()
#Text in Sätze aufspalten
tokenized = custom_sent_tokenizer.tokenize(raw_text)
#print(tokenized)

#jeden Satz durchgehen
for sentence in tokenized:
    #Satz tokenizen
    words = nltk.word_tokenize(sentence)

    #jedes Wort im Satz durchgehen
    for word in words:
        for synonym in synonyms:
            #vergleichen ob Wort mit Synonym übereinstimmt
            if synonym in word:
                sentenceList.append(sentence)
                
foundSentences = [()]
#gefundenen Sätze tokenizen, taggen, Verb mit Verbliste überprüfen
for sentence in sentenceList:
    #print(sentence)
    words = nltk.word_tokenize(sentence)
    #Datentyp: Liste mit Tupeln
    tagged_sentence = nltk.pos_tag(words)
    #print(tagged_sentence)
    for (word, tag) in tagged_sentence:
        if tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            # !!!!Verb auf stamm reduzieren!!!!
            for synonym in synonyms:
                if synonym in word:
                    foundSentences.append(tagged_sentence)
                    #print(tagged_sentence)
                    #print(word,tag)
                    ## weiteres Vorgehen:
                    ## Subjekt und Objekt aus dem Satz entnehmen
                    ## als zB. Tupel in einer Liste speichern
                    ## gesamte Liste zeigt dann alle "Tötungspaare"

for sentence in foundSentences:
    
    #Jeder Satz als Tree mit POS-Tag
    namedEnt = nltk.ne_chunk(sentence, binary=True)
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
    print(docs)

    

    
##    namedEnt = nltk.ne_chunk(tagged_sentence, binary = True)
##    chunkGram = r"""Chunk: {<.*>+<VB.?>+<.*>}"""
####    chunkGram = r"""Chunk: {<NE>+<.*>*<VB.?>+<.*>*<NE>|<PRP>+<.*>*<VB.?>+<.*>*<NE>}"""
##    chunkParser = nltk.RegexpParser(chunkGram)
##    chunked_sentence = chunkParser.parse(namedEnt)
##    docs = []
##    for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'Chunk'):
##        docs.append(" ".join([a for (a,b) in subtree.leaves()]))
##        #subtree.draw()
                                    
    #print(tagged_sentence)
    


                
        
    


