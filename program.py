import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk, pos_tag

# Lemmatizer: macht aus dogs -> dog usw.
wordnet_lemmatizer = WordNetLemmatizer()
# Satz Tokenizer: speichert jeden Satz in einem Eintrag in einer Liste
sent_tokenizer = PunktSentenceTokenizer()
# alle Verb-Tags die es gibt
verb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

'''
TODO
In einem anderen Programm sollen alle namedEntities aus den Büchern ausgelesen
werden (Doppelte aussortieren!). Diese Liste korrigieren wir manuell und
speichern sie in einer Textdatei. Dann müssen wir eine Möglichkeit finden,
Namen die aus mehr als einem Wort bestehen als einen Namen zu kennzeichnen.
'''
namedEntities_text = open("namedEntities.txt", "r").read()
namedEntities = nltk.word_tokenize(namedEntities_text)
'''
TODO
Eine Liste mit sinnvollen Synonymen zusammenstellen und in einer Textdatei
speichern.
'''
synonyms_text = open("synonyms.txt", "r").read()
synonyms = nltk.word_tokenize(synonyms_text)

# text tokenizen und in Dictionary speichern
text = open("buch_ausschnitt.txt", "r").read()
tokenized = sent_tokenizer.tokenize(text)
tagged_text = {}
found_sentences = {}
counter = 1

for sentence in tokenized:
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
    dic1 = {counter:tagged_words}  
    tagged_text.update(dic1)

    # alle Sätze mit einem kill-Synonym werden in einem weiteren Dictionary gespeichert
    for (word, tag) in tagged_words:
        if tag in verb_tags:
            lemma = wordnet_lemmatizer.lemmatize(word, pos='v')
            if lemma in synonyms:
                dic2 = {counter:tagged_words}
                found_sentences.update(dic2)
    counter += 1
    
print("*****************************NORMALES WÖRTERBUCH************************")
for eintrag in tagged_text:
    print (eintrag, tagged_text[eintrag])
print("********************************GEFUNDENE SÄTZE*************************")
for eintrag2 in found_sentences:
    print (eintrag2, found_sentences[eintrag2])

##for sentence in found_sentences:
##    chunk = ne_chunk(pos_tag(found_sentences[sentence]))
##    print(chunk)
##    #chunk.draw()

print("**********************Gefundene Verben, Subjekte, Objekte****************")
count = 1
for entry in found_sentences:
    sentence = found_sentences[entry]
    for (word, tag) in sentence:
        if tag in verb_tags:
            lemma = wordnet_lemmatizer.lemmatize(word, pos='v')

            # kill-Synonym wird aus dem Satz herausgesucht
            if lemma in synonyms:
                verb_index = sentence.index((word, tag))
                print ("Verb-Index: ", verb_index, " Verb: ", word)


                # Vor dem Verb werden Named Entities gesucht, sie sind potenzielle Subjekte
                for count_steps in range(1, 11):
                    if(verb_index-count_steps >= 0):
                        potential_subject_tuple = sentence[verb_index-count_steps]
                        potential_subject = potential_subject_tuple[0]
                        if potential_subject in namedEntities:
                            print ("Potenzielles Subjekt: ", potential_subject, "(", count_steps, " Stelle(n) entfernt)")
                            
                # Nach dem Verb werden Named Entities gesucht, sie sind potenzielle Objekte
                for count_steps in range(1, 11):
                    if(verb_index+count_steps <= sentence.index(max(sentence))):
                        potential_object_tuple = sentence[verb_index+count_steps]
                        potential_object = potential_object_tuple[0]
                        if potential_object in namedEntities:
                            print ("Potenzielles Objekt: ", potential_object, "(", count_steps, " Stelle(n) entfernt)")
                
                print(sentence)
                print("*****************************************************************")

                
                
    
    
    
    
    

